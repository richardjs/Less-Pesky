import os

from PIL import Image

IMAGE_DIR = 'images'

def median(l):
	# Fudging it when there's an even number of items...
	return sorted(l)[len(l)/2]

size_x = None
size_y = None
values = None
for filename in os.listdir(IMAGE_DIR):
	print 'Reading', filename
	image = Image.open(os.path.join(IMAGE_DIR, filename))
	size_x, size_y = image.size
	
	if not values:
		values = [
			[[[], [], []] for _ in range(size_x)] for _ in range(size_y)
		]
	
	for y in range(size_y):
		for x in range(size_x):
			r, g, b = image.getpixel((x, y))
			values[y][x][0].append(r)
			values[y][x][1].append(g)
			values[y][x][2].append(b)

print 'Creating new image'
image = Image.new('RGB', (size_x, size_y))
for y in range(size_y):
	for x in range(size_x):
		r_values = values[y][x][0]
		g_values = values[y][x][1]
		b_values = values[y][x][2]

		r = median(r_values)
		g = median(g_values)
		b = median(b_values)

		image.putpixel((x, y), (r, g, b))

print 'Saving image'
image.save('output.png')
