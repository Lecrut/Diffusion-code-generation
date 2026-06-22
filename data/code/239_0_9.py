class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @staticmethod
    def calculate_perimeter(width, height):
        return 2 * (width + height)

if __name__ == '__main__':
    rect = Rectangle(5, 3)
    perimeter = rect.calculate_perimeter(rect.width, rect.height)
    print(perimeter)