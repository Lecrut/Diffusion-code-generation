class Shape:
    RECTANGLE = "rectangle"
    TRIANGLE = "triangle"

    def __init__(self, shape_type):
        self.shape_type = shape_type.lower()
    
    @staticmethod
    def calculate_rectangle_area(width, height):
        return width * height
    
    @staticmethod
    def calculate_triangle_area(base, height):
        return 0.5 * base * height

    def area(self, dimension1, dimension2):
        if self.shape_type == Shape.RECTANGLE:
            return Shape.calculate_rectangle_area(dimension1, dimension2)
        elif self.shape_type == Shape.TRIANGLE:
            return Shape.calculate_triangle_area(dimension1, dimension2)
        else:
            raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    rectangle = Shape(Shape.RECTANGLE)
    rect_width = 10
    rect_height = 5
    print(f"Rectangle Area: {rectangle.area(rect_width, rect_height)}")
    
    triangle = Shape(Shape.TRIANGLE)
    tri_base = 8
    tri_height = 6
    print(f"Triangle Area: {triangle.area(tri_base, tri_height)}")