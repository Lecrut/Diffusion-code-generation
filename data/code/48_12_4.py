class Shape:
    def __init__(self, shape_type, side1, side2=None, side3=None):
        self.shape_type = shape_type
        if shape_type == "rectangle":
            self.side1 = side1
            self.side2 = side2
        elif shape_type == "triangle":
            self.side1 = side1
            self.side2 = side2
            self.side3 = side3
        else:
            raise ValueError("Invalid shape type")
    def calculate_perimeter(self):
        if self.shape_type == "rectangle":
            return 2 * (self.side1 + self.side2)
        elif self.shape_type == "triangle":
            return self.side1 + self.side2 + self.side3
        else:
            return 0
    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.side1 * self.side2
        elif self.shape_type == "triangle":
            if self.side3 is not None:
                return 0.5 * (self.side1 * self.side2)
            else:
                return 0
        else:
            return 0
if __name__ == '__main__':
    rectangle = Shape("rectangle", 10, 5)
    triangle = Shape("triangle", 4, 5, 6)
    print("Rectangle:")
    print("Perimeter:", rectangle.calculate_perimeter())
    print("Area:", rectangle.calculate_area())
    print("\nTriangle:")
    print("Perimeter:", triangle.calculate_perimeter())
    print("Area:", triangle.calculate_area())