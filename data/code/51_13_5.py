import math

class Circle:
    PI = math.pi
    
    @staticmethod
    def calculate_perimeter(radius):
        return 2 * Circle.PI * radius

if __name__ == '__main__':
    hard_coded_radius = 10.0
    circle = Circle()
    perimeter = circle.calculate_perimeter(hard_coded_radius)
    print(perimeter)