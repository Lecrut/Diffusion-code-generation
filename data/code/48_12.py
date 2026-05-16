class Shape:
    def __init__(self, shape_type, side_length):
        self.shape_type = shape_type
        self.side_length = side_length
    def calculate_perimeter(self):
        if self.shape_type == "rectangle":
            return 2 * (self.side_length + self.side_length)
        elif self.shape_type == "square":
            return 4 * self.side_length
        else:
            return 0
    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.side_length * self.side_length
        elif self.shape_type == "square":
            return self.side_length * self.side_length
        else:
            return 0
if __name__ == '__main__':
    shape1 = Shape("rectangle", 5)
    shape2 = Shape("square", 4)
    print("Shape 1 (Rectangle):")
    print("Perimeter:", shape1.calculate_perimeter())
    print("Area:", shape1.calculate_area())
    print("\nShape 2 (Square):")
    print("Perimeter:", shape2.calculate_perimeter())
    print("Area:", shape2.calculate_area())