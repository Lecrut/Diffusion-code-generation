import math

class CircleCalculator:
    PI = math.pi
    
    @staticmethod
    def calculate_area(radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        return CircleCalculator.PI * (radius ** 2)

if __name__ == '__main__':
    sample_radius = 3.0
    try:
        area = CircleCalculator.calculate_area(sample_radius)
        print(area)
    except ValueError as e:
        print(f"Error: {e}")