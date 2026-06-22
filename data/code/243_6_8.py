import math

class Circle:
    RADIUS = 100
    
    @staticmethod
    def calculate_perimeter(radius):
        return 2 * math.pi * radius

if __name__ == '__main__':
    perimeter = Circle.calculate_perimeter(Circle.RADIUS)
    print(perimeter)