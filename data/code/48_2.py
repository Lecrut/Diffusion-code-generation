class Shape:
    def __init__(self, shape_type, side1, side2=None):
        self.shape_type = shape_type
        if shape_type == "square":
            self.side1 = side1
        elif shape_type == "rectangle":
            self.side1 = side1
            self.side2 = side2
        else:
            raise ValueError("Invalid shape type")
    def calculate_perimeter(self):
        if self.shape_type == "square":
            return 4 * self.side1
        elif self.shape_type == "rectangle":
            return 2 * (self.side1 + self.side2)
        else:
            return 0
    def calculate_area(self):
        if self.shape_type == "square":
            return self.side1 * self.side1
        elif self.shape_type == "rectangle":
            return self.side1 * self.side2
        else:
            return 0
if __name__ == '__main__':
    square = Shape("square", 5)
    rectangle = Shape("rectangle", 4, 6)
    print("Square:")
    print("Perimeter:", square.calculate_perimeter())
    print("Area:", square.calculate_area())
    print("\nRectangle:")
    print("Perimeter:", rectangle.calculate_perimeter())
    print("Area:", rectangle.calculate_area())