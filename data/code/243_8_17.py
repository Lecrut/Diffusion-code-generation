import math

class Circle:
    PI = 2 * math.pi
    
    @staticmethod
    def calculate_perimeter(radius):
        return Circle.PI * radius

if __name__ == '__main__':
    sample_radius = 10
    perimeter = Circle.calculate_perimeter(sample_radius)
    print(f"Perimeter: {perimeter}")