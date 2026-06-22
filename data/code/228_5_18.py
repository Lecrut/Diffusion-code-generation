import math

TRIANGLE_ROWS = 6

def draw_isosceles_triangle(rows):
    for i in range(rows):
        spaces = ' ' * (rows - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)

if __name__ == '__main__':
    draw_isosceles_triangle(TRIANGLE_ROWS)