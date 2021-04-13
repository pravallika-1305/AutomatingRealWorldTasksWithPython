from PIL import Image

filename = 'landscape.jpg'
filepath = f"original_images/{filename}"

# Load the original image, and get its size and color mode.
orig_image = Image.open(filepath)
width, height = orig_image.size
mode = orig_image.mode

print(f"Original image: {filename}")
print(f"Size: {width} x {height} pixels")
print(f"Mode: {mode}")

# Load all pixels from the image.
orig_pixel_map = orig_image.load()

# Look at the pixel in the top left corner.
first = orig_pixel_map[0, 0]
print(f"\nFirst pixel: {first}")
