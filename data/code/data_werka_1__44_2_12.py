class Rectangle:
    LENGTH = 15
    WIDTH = 8

    @staticmethod
    def calculate_perimeter(length, width):
        return 2 * (length + width)

if __name__ == '__main__':
    perimeter = Rectangle.calculate_perimeter(Rectangle.LENGTH, Rectangle.WIDTH)
    print(perimeter)