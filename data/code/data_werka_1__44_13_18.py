class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @staticmethod
    def calculate_perimeter(length, width):
        return 2 * (length + width)

if __name__ == '__main__':
    L_val = 8
    W_val = 6
    rectangle = Rectangle(L_val, W_val)
    perimeter = Rectangle.calculate_perimeter(rectangle.length, rectangle.width)
    print(perimeter)