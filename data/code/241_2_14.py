class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def is_valid_dimensions(self):
        if self.length <= 0 or self.width <= 0:
            raise ValueError("Length and width must be positive numbers.")
    
    def area(self):
        self.is_valid_dimensions()
        return self.length * self.width

if __name__ == '__main__':
    rect = Rectangle(10, 5)
    area_result = rect.area()
    print(area_result)