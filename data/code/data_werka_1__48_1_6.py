class Shape:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width is not None else length

    @staticmethod
    def square_perimeter(side_length):
        return 4 * side_length

    @staticmethod
    def square_area(side_length):
        return side_length ** 2

    @staticmethod
    def rectangle_perimeter(length, width):
        return 2 * (length + width)

    @staticmethod
    def rectangle_area(length, width):
        return length * width

if __name__ == '__main__':
    square_side = 5
    rectangle_length = 4
    rectangle_width = 6

    print("Square Perimeter:", Shape.square_perimeter(square_side))
    print("Square Area:", Shape.square_area(square_side))
    print("Rectangle Perimeter:", Shape.rectangle_perimeter(rectangle_length, rectangle_width))
    print("Rectangle Area:", Shape.rectangle_area(rectangle_length, rectangle_width))