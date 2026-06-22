class Shapes:
    @staticmethod
    def kite_area(d1, d2):
        return 0.5 * d1 * d2

    @staticmethod
    def circle_area(radius):
        import math
        return math.pi * radius ** 2

if __name__ == '__main__':
    shapes = Shapes()
    kite_d1 = 4
    kite_d2 = 6
    circle_radius = 5 / 2
    kite_area = shapes.kite_area(kite_d1, kite_d2)
    circle_area = shapes.circle_area(circle_radius)
    total_area = kite_area + circle_area
    print(total_area)