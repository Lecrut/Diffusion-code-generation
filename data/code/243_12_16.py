import math

class Circle:
    PI = math.pi
    
    @staticmethod
    def calculate_perimeter(diameter):
        return diameter * Circle.PI

if __name__ == '__main__':
    sample_diameter = 25
    perimeter = Circle.calculate_perimeter(sample_diameter)
    print(perimeter)