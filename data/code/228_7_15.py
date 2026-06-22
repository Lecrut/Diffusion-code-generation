from PIL import Image

def create_colored_triangle_image(width=500, height=500):
    triangle_color = (255, 0, 0)
    background_color = (255, 255, 255)
    img = Image.new('RGB', (width, height), background_color)
    point1 = (width // 4, height)
    point2 = (width * 3 // 4, height)
    point3 = (width // 2, height // 4)
    points = [point1, point2, point3]
    draw = ImageDraw.Draw(img)
    draw.polygon(points, fill=triangle_color)
    return img
if __name__ == '__main__':
    triangle_image = create_colored_triangle_image()
    triangle_image.save('colored_triangle.png')
    triangle_image.show()