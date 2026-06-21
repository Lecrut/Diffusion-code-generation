import math

class GeometryCalculator:
    @staticmethod
    def circle_area(radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_radius = 5
    area = GeometryCalculator.circle_area(sample_radius)
    print(f"Area of the circle with radius {sample_radius}: {area}")