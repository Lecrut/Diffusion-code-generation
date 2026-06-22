import math

class Circle:
    PI = math.pi

    @staticmethod
    def calculate_perimeter(radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return 2 * Circle.PI * radius

if __name__ == '__main__':
    sample_radius = 4.25
    circle = Circle()
    perimeter = circle.calculate_perimeter(sample_radius)
    print(perimeter)