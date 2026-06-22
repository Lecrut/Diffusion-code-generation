class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

def compare_shapes(rectangle, square):
    comparison = {
        "rectangle_area": rectangle.area(),
        "rectangle_perimeter": rectangle.perimeter(),
        "square_area": square.area(),
        "square_perimeter": square.perimeter()
    }
    return comparison

if __name__ == '__main__':
    side_length = 5
    rectangle = Rectangle(8, 6)
    square = Square(side_length)
    result = compare_shapes(rectangle, square)
    print(result)