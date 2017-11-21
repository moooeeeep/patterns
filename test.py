from PIL import Image
import itertools

def get_origin(col, row, pattern_size, margin):
	""" produces the origin position of the pattern at the specified grid pos
	"""
	w,h = pattern_size
	origin = col*(w+margin), row*(h+margin)
	return origin

def make_pattern(pixels, origin, pattern_size, ndots):
	""" assigns the pixels for the pattern to image data region """
	w,h = pattern_size
	ow,oh = origin
	coordinates = itertools.product(range(h), range(w))
	with_offset = [(c+ow, r+oh) for r,c in coordinates]
	# take only n dots
	with_offset = with_offset[:ndots]
	for c,r in with_offset:
		pixels[c, r] = 0

# calculate image size from pattern dimensions and number of patterns
pattern_width, pattern_height = 10, 10
pattern_size = pattern_width, pattern_height
n_cols, n_rows = 7, 10
margin = 10
image_size = (pattern_width+margin)*n_cols-margin, (pattern_height+margin)*n_rows-margin

# create image
img = Image.new('L', image_size, "white") # 'L' for grayscale, initialize white
pixels = img.load() # create the pixel map

# write image data
for n_dots,rc in enumerate(itertools.product(range(n_rows), range(n_cols)), 1):
	r,c = rc
	n_dots = 100 - n_dots
	origin = get_origin(c, r, pattern_size, margin)
	make_pattern(pixels, origin, pattern_size, n_dots)

img.save("test.bmp")
