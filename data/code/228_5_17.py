class AsciiTriangle:
    @staticmethod
    def print_isosceles_triangle(height):
        width = 2 * height - 1
        for i in range(height):
            spaces = ' ' * (height - i - 1)
            stars = '*' * (2 * i + 1)
            print(spaces + stars)

if __name__ == '__main__':
    triangle_height = 5
    AsciiTriangle.print_isosceles_triangle(triangle_height)