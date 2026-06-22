class Rectangle:
    def __init__(self, length, width):
        if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
            raise ValueError("Length and width must be numbers")
        if length < 0 or width < 0:
            raise ValueError("Length and width must be non-negative")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

if __name__ == '__main__':
    rect = Rectangle(10, 5)
    area_result = rect.area()
    print(area_result)