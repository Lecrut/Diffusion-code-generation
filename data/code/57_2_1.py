class Shape:
    def calculate_area(self, shape_type, *args):
        if shape_type == "circle":
            radius = args[0]
            return 3.14159 * radius**2
        elif shape_type == "rectangle":
            length = args[0]
            width = args[1]
            return length * width
        else:
            raise ValueError("Unsupported shape type")
if __name__ == '__main__':
    shape_calculator = Shape()
    circle_area = shape_calculator.calculate_area("circle", 5)
    print(f"Area of circle with radius 5: {circle_area}")
    rectangle_area = shape_calculator.calculate_area("rectangle", 10, 4)
    print(f"Area of rectangle with length 10 and width 4: {rectangle_area}")