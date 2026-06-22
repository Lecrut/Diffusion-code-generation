import math

class EquilateralTriangle:
    SQRT_3 = math.sqrt(3)
    
    def __init__(self, height):
        if height <= 0:
            raise ValueError("Height must be positive")
        self.height = height
        self.side_length = self.calculate_side_length()
        self.perimeter = self.calculate_perimeter()
    
    @staticmethod
    def calculate_side_length(height):
        return (2 * height) / EquilateralTriangle.SQRT_3
    
    @staticmethod
    def calculate_perimeter(side_length):
        return 3 * side_length
    
    def get_side_length(self):
        return self.side_length
    
    def get_perimeter(self):
        return self.perimeter

if __name__ == '__main__':
    try:
        triangle = EquilateralTriangle(height=8.73)
        print(f'Side Length: {triangle.get_side_length()}')
        print(f'Perimeter: {triangle.get_perimeter()}')
    except ValueError as e:
        print(e)