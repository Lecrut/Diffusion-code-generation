class Shape:
    def __init__(self, side_length):
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        self.side_length = side_length

    def perimeter(self):
        return 4 * self.side_length

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(width)
        if height <= 0:
            raise ValueError("Height must be positive")
        self.height = height

    def area(self):
        return self.side_length * self.height

class Square(Shape):
    def area(self):
        return self.side_length ** 2

def compare_shapes(rectangle, square):
    comparison = {
        "rectangle": {
            "area": rectangle.area(),
            "perimeter": rectangle.perimeter()
        },
        "square": {
            "area": square.area(),
            "perimeter": square.perimeter()
        }
    }
    return comparison

if __name__ == '__main__':
    side_length = 5
    rectangle = Rectangle(side_length, side_length)
    square = Square(side_length)
    result = compare_shapes(rectangle, square)
    print(result)