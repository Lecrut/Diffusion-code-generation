TRIANGLE_HEIGHT = 5
TRIANGLE_BASE = 9

def draw_isosceles_triangle(height, base):
    for i in range(height):
        spaces = ' ' * (base // 2 - i)
        stars = '*' * (i * 2 + 1)
        print(spaces + stars)

if __name__ == '__main__':
    draw_isosceles_triangle(TRIANGLE_HEIGHT, TRIANGLE_BASE)