class Rectangle:
    LENGTH = 12
    WIDTH = 6

    @staticmethod
    def calculate_perimeter(length, width):
        return 2 * (length + width)

if __name__ == '__main__':
    perimeter = Rectangle.calculate_perimeter(Rectangle.LENGTH, Rectangle.WIDTH)
    print(perimeter)