import math

class Circle:
    PI = math.pi

    @staticmethod
    def calculate_perimeter(radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return 2 * Circle.PI * radius

if __name__ == '__main__':
    hard_coded_radius = 4.5
    try:
        perimeter = Circle.calculate_perimeter(hard_coded_radius)
        print(perimeter)
    except ValueError as e:
        print(e)