import math

class Circle:
    PI = 2 * math.pi
    
    @staticmethod
    def calculate_circumference(radius):
        return Circle.PI * radius

if __name__ == '__main__':
    sample_radius = 5.0
    circumference_result = Circle.calculate_circumference(sample_radius)
    print(circumference_result)