class GeometryUtils:
    PI = 3.14159

    @staticmethod
    def calculate_perimeter(shape, *dimensions):
        perimeter_calculators = {
            'rectangle': GeometryUtils._calculate_rectangle_perimeter,
            'circle': GeometryUtils._calculate_circle_perimeter
        }
        
        if shape not in perimeter_calculators:
            raise ValueError(f"Unsupported shape: {shape}")
        
        return perimeter_calculators[shape](*dimensions)

    @staticmethod
    def _calculate_rectangle_perimeter(length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        return 2 * (length + width)

    @staticmethod
    def _calculate_circle_perimeter(radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        return 2 * GeometryUtils.PI * radius

if __name__ == '__main__':
    rectangle_perimeter = GeometryUtils.calculate_perimeter('rectangle', 5, 3)
    circle_perimeter = GeometryUtils.calculate_perimeter('circle', 7)
    
    print(f"Rectangle Perimeter: {rectangle_perimeter}")
    print(f"Circle Perimeter: {circle_perimeter}")