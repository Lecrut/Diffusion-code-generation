import math

class Circle:
    PI = math.pi

    @staticmethod
    def calculate_area(radius):
        return Circle.PI * radius ** 2

if __name__ == '__main__':
    test_cases = [
        (1, Circle.PI),
        (2, 4 * Circle.PI),
        (0, 0),
        (10, 100 * Circle.PI),
        (5.5, 30.25 * Circle.PI)
    ]
    for radius, expected in test_cases:
        result = Circle.calculate_area(radius)
        print(f"Radius: {radius}, Expected Area: {expected}, Calculated Area: {result}")