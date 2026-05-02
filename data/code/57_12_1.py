class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type
    def calculate_area(self):
        if self.shape_type == 'rectangle':
            length = 10
            width = 5
            return length * width
        elif self.shape_type == 'triangle':
            base = 7
            height = 4
            return 0.5 * base * height
        else:
            return 0
if __name__ == '__main__':
    rectangle_shape = Shape('rectangle')
    triangle_shape = Shape('triangle')
    rectangle_area = rectangle_shape.calculate_area()
    triangle_area = triangle_shape.calculate_area()
    print(f"Rectangle Area: {rectangle_area}")
    print(f"Triangle Area: {triangle_area}")