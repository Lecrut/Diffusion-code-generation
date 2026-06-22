def draw_isosceles_triangle(height):
    if not isinstance(height, int) or height <= 0:
        raise ValueError("Height must be a positive integer")
    
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

if __name__ == '__main__':
    draw_isosceles_triangle(5)