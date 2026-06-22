import math

class Circle:
    PI = math.pi

    @staticmethod
    def calculate_area(radius):
        return Circle.PI * radius ** 2

if __name__ == '__main__':
    sample_radius = 7
    area = Circle.calculate_area(sample_radius)
    print(area)