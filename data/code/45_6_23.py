import math

class Circle:
    PI = math.pi
    
    @staticmethod
    def area(radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return Circle.PI * (radius ** 2)

if __name__ == '__main__':
    sample_values = [3, 7, 1.5, 0]
    for value in sample_values:
        try:
            area = Circle.area(value)
            print(f"Area of circle with radius {value}: {area}")
        except ValueError as e:
            print(e)