import math

class CircleCalculator:
    RADIUS = 100
    
    @staticmethod
    def calculate_perimeter(radius=RADIUS):
        return float(2 * math.pi * radius)

if __name__ == '__main__':
    print(CircleCalculator.calculate_perimeter())