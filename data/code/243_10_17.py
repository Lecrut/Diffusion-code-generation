import math

class CircleMath:
    PI = math.pi
    
    @staticmethod
    def calculate_circle_perimeter(radius):
        return 2 * CircleMath.PI * radius

if __name__ == '__main__':
    sample_radius = 5.0
    perimeter = CircleMath.calculate_circle_perimeter(sample_radius)
    print(perimeter)