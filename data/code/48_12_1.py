class Shape:
    def __init__(self, shape_type, side1, side2, side3, side4=None):
        self.shape_type = shape_type
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4
    def calculate_perimeter(self):
        if self.shape_type == "rectangle":
            return 2 * (self.side1 + self.side2)
        elif self.shape_type == "square":
            return 4 * self.side1
        elif self.shape_type == "triangle":
            return self.side1 + self.side2 + self.side3
        else:
            return 0
    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.side1 * self.side2
        elif self.shape_type == "square":
            return self.side1 * self.side1
        elif self.shape_type == "triangle":
            return 0.5 * (self.side1 + self.side2 + self.side3)
        else:
            return 0
if __name__ == '__main__':
    rectangle = Shape("rectangle", 10, 5, 10)
    square = Shape("square", 7, 7, 7, 7)
    triangle = Shape("triangle", 4, 5, 6)
    print("Rectangle Perimeter:", rectangle.calculate_perimeter())
    print("Rectangle Area:", rectangle.calculate_area())
    print("Square Perimeter:", square.calculate_perimeter())
    print("Square Area:", square.calculate_area())
    print("Triangle Perimeter:", triangle.calculate_perimeter())
    print("Triangle Area:", triangle.calculate_area())