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
    print("Rectangle:")
    print("Perimeter:", rectangle.calculate_perimeter())
    print("Area:", rectangle.calculate_area())
    print("\nSquare:")
    print("Perimeter:", square.calculate_perimeter())
    print("Area:", square.calculate_area())