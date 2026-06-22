import math

class Circle:
    PI = math.pi
    
    @staticmethod
    def perimeter(diameter):
        return diameter * Circle.PI

if __name__ == '__main__':
    sample_diameter = 30
    perimeter = Circle.perimeter(sample_diameter)
    print(perimeter)