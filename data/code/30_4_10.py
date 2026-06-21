import math

class Circle:
    RADIUS = 7

    @staticmethod
    def compute_area(r):
        squared = r * r
        return math.pi * squared

if __name__ == '__main__':
    current_radius = Circle.RADIUS
    result = Circle.compute_area(current_radius)
    print(result)