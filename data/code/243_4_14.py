import math

class Circle:
    PI = math.pi

    @staticmethod
    def calculate_perimeter(radius):
        return 2 * Circle.PI * radius

if __name__ == '__main__':
    sample_radius = 5.0
    perimeter = Circle.calculate_perimeter(sample_radius)
    print(perimeter)