class Shape:
    def __init__(self, shape_type, length, width, base, height):
        self.shape_type = shape_type
        if shape_type == 'rectangle':
            self.length = length
            self.width = width
        elif shape_type == 'triangle':
            self.base = base
            self.height = height
        else:
            raise ValueError("Invalid shape type")
    def calculate_area(self):
        if self.shape_type == 'rectangle':
            return self.length * self.width
        elif self.shape_type == 'triangle':
            return 0.5 * self.base * self.height
        else:
            return 0
if __name__ == '__main__':
    rectangle = Shape('rectangle', 10, 5, 0, 0)
    triangle = Shape('triangle', 4, 6, 0, 0)
    rectangle_area = rectangle.calculate_area()
    triangle_area = triangle.calculate_area()
    print(f"Rectangle Area: {rectangle_area}")
    print(f"Triangle Area: {triangle_area}")