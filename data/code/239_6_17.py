class Rectangle:
    @staticmethod
    def calculate_perimeter(width, height):
        return 2 * (width + height)

if __name__ == '__main__':
    width = 10
    height = 5
    perimeter = Rectangle.calculate_perimeter(width, height)
    print(perimeter)