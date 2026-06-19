import math

class Circle:
    PI = math.pi

    @staticmethod
    def area(radius):
        return Circle.PI * (radius ** 2)

if __name__ == '__main__':
    sample_radius = 12
    circle_instance = Circle()
    print(circle_instance.area(sample_radius))