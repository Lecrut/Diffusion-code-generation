import math

class CircleCalculator:
    PI = math.pi
    
    @staticmethod
    def calculate_circumference(radius):
        return 2 * CircleCalculator.PI * radius

if __name__ == '__main__':
    sample_radius = 2.5
    circumference = CircleCalculator.calculate_circumference(sample_radius)
    print(circumference)