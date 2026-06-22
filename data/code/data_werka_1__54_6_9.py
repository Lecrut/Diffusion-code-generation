import math

class Circle:
    @staticmethod
    def calculate_area(radius):
        return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_radius = 3
    result = Circle.calculate_area(sample_radius)
    print(result)