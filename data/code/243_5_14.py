import math

class Circle:
    PI = 3.141592653589793
    
    @staticmethod
    def calculate_circumference(radius):
        return 2 * Circle.PI * radius

if __name__ == '__main__':
    sample_radius = 2.5
    circumference = Circle.calculate_circumference(sample_radius)
    print(circumference)