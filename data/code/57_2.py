class Shape:
    def calculate_area(self, shape_type, **kwargs):
        if shape_type == "circle":
            radius = kwargs.get("radius")
            if radius is not None:
                return 3.14159 * radius**2
        elif shape_type == "rectangle":
            length = kwargs.get("length")
            width = kwargs.get("width")
            if length is not None and width is not None:
                return length * width
        else:
            return "Unknown shape type"
if __name__ == '__main__':
    my_shape = Shape()
    circle_area = my_shape.calculate_area("circle", radius=5)
    print(f"Circle Area: {circle_area}")
    rectangle_area = my_shape.calculate_area("rectangle", length=10, width=4)
    print(f"Rectangle Area: {rectangle_area}")
    unknown_area = my_shape.calculate_area("triangle", base=5, height=10)
    print(f"Triangle Area: {unknown_area}")