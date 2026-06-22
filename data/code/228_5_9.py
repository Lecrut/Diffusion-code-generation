def draw_isosceles_triangle(height):
    for i in range(1, height + 1):
        print(' ' * (height - i) + '*' * (2 * i - 1))

if __name__ == '__main__':
    triangle_height = 5
    draw_isosceles_triangle(triangle_height)