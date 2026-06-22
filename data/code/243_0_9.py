import math

class Circle:
    PI = math.pi

    @staticmethod
    def calculate_circumference(radius: float) -> float:
        return 2 * Circle.PI * radius

if __name__ == '__main__':
    sample_radius = 5.0
    circumference = Circle.calculate_circumference(sample_radius)
    print(circumference)