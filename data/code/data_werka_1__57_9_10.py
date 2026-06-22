class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type.lower()
    
    def area(self, *dimensions):
        if not dimensions:
            raise ValueError("Dimensions are required to calculate area")
        
        if self.shape_type == 'rectangle':
            return self._rectangle_area(*dimensions)
        elif self.shape_type == 'triangle':
            return self._triangle_area(*dimensions)
        else:
            raise ValueError('Unsupported shape type')
    
    def _rectangle_area(self, width, height):
        return width * height
    
    def _triangle_area(self, base, height):
        return 0.5 * base * height

if __name__ == '__main__':
    rectangle = Shape('rectangle')
    rect_area = rectangle.area(10, 5)
    print(f"Rectangle area: {rect_area}")

    triangle = Shape('triangle')
    tri_area = triangle.area(8, 4)
    print(f"Triangle area: {tri_area}")