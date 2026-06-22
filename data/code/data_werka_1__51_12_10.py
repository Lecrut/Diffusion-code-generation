class Rectangle:
    WIDTH = 5
    HEIGHT = 10

    @staticmethod
    def calculate_perimeter(width, height):
        return 2 * (width + height)

if __name__ == '__main__':
    width = Rectangle.WIDTH
    height = Rectangle.HEIGHT
    perimeter = Rectangle.calculate_perimeter(width, height)
    print(perimeter)