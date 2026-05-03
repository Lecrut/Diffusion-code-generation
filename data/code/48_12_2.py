class Shape:
    def __init__(self, shape_type, side1, side2):
        self.shape_type = shape_type
        self.side1 = side1
        self.side2 = side2
    def calculate_perimeter(self):
        if self.shape_type == "rectangle":
            return 2 * (self.side1 + self.side2)
        elif self.shape_type == "square":
            return 4 * self.side1
        else:
            return 0
    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.side1 * self.side2
        elif self.shape_type == "square":
            return self.side1 * self.side1
        else:
            return 0
if __name__ == '__main__':
    rectangle = Shape("rectangle", 10, 5)
    square = Shape("square", 7, 7)
    rectangle_perimeter = rectangle.calculate_perimeter()
    rectangle_area = rectangle.calculate_area()
    square_perimeter = square.calculate_perimeter()
    square_area = square.calculate_area()
    print(f"Rectangle Perimeter: {rectangle_perimeter}")
    print(f"Rectangle Area: {rectangle_area}")
    print(f"Square Perimeter: {square_perimeter}")
    print(f"Square Area: {square_area}")