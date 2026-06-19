import math

class Circle:
    PI = math.pi

    @staticmethod
    def calculate_area(radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        return Circle.PI * (radius ** 2)

if __name__ == '__main__':
    try:
        sample_radius = 8
        area = Circle.calculate_area(sample_radius)
        print(area)
    except ValueError as e:
        print(f"Error: {e}")