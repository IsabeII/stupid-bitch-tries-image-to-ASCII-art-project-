from PIL import Image
image_path = 'C:\\Users\\user\\Desktop\\Buba.jpg' 
image = Image.open(image_path)
ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
intensity = 255 // (len(ascii_chars) - 1)
ascii_art = ""
width, height = image.size
for y in range(height):
    for x in range(width):
        r, g, b = image.getpixel((x, y))
        gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
        char_index = min(gray // intensity, len(ascii_chars) - 1)
        ascii_art += ascii_chars[char_index]
    ascii_art += "\n"
print(ascii_art)
