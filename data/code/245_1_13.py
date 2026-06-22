import math

class AreaComparer:
    @staticmethod
    def calculate_circle_area(radius):
        return math.pi * (radius ** 2)

    @staticmethod
    def calculate_square_area(length):
        return length * length

    @classmethod
    def check_equal_areas(cls, radius, length):
        circle_area = cls.calculate_circle_area(radius)
        square_area = cls.calculate_square_area(length)
        return circle_area == square_area

if __name__ == '__main__':
    r1 = 5.0
    l1 = 25.0
    print(f"Radius: {r1}, Length: {l1}, Areas Equal: {AreaComparer.check_equal_areas(r1, l1)}")

    r2 = 1.0
    l2 = math.pi
    print(f"Radius: {r2}, Length: {l2}, Areas Equal: {AreaComparer.check_equal_areas(r2, l2)}")

    r3 = 3.0
    l3 = 9.0
    print(f"Radius: {r3}, Length: {l3}, Areas Equal: {AreaComparer.check_equal_areas(r3, l3)}")