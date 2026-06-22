def draw_isosceles_triangle(height):
    if height <= 0:
        raise ValueError("Height must be greater than zero")
    
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

if __name__ == '__main__':
    triangle_height = 5
    draw_isosceles_triangle(triangle_height)