class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type.lower()
        if self.shape_type not in ['rectangle', 'triangle']:
            raise ValueError("Unsupported shape type. Please use 'rectangle' or 'triangle'.")
    
    def area(self, *args):
        if self.shape_type == 'rectangle':
            return self._calculate_rectangle_area(*args)
        elif self.shape_type == 'triangle':
            return self._calculate_triangle_area(*args)
    
    def _validate_dimensions(self, args, expected_count):
        if len(args) != expected_count:
            raise ValueError(f"{self.shape_type.capitalize()} requires {expected_count} dimensions.")
    
    def _calculate_rectangle_area(self, width, height):
        self._validate_dimensions((width, height), 2)
        return width * height
    
    def _calculate_triangle_area(self, base, height):
        self._validate_dimensions((base, height), 2)
        return 0.5 * base * height

if __name__ == '__main__':
    rectangle = Shape('rectangle')
    print("Rectangle Area:", rectangle.area(10, 5))

    triangle = Shape('triangle')
    print("Triangle Area:", triangle.area(8, 4))