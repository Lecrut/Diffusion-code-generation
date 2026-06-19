class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type.lower()
    
    def area(self, *dimensions):
        if self.shape_type == 'rectangle':
            return self._calculate_rectangle_area(*dimensions)
        elif self.shape_type == 'triangle':
            return self._calculate_triangle_area(*dimensions)
        else:
            raise ValueError('Unsupported shape type')
    
    def _calculate_rectangle_area(self, width, height):
        return width * height
    
    def _calculate_triangle_area(self, base, height):
        return 0.5 * base * height

if __name__ == '__main__':
    triangle = Shape('triangle')
    base_length = 8
    height_length = 12
    print(f"Triangle area with base {base_length} and height {height_length}: {triangle.area(base_length, height_length)}")