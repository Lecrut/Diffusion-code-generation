import math

class AreaCalculator:
    @staticmethod
    def calculate_semicircle_area(radius):
        return 0.5 * math.pi * (radius ** 2)

    @staticmethod
    def calculate_rectangle_area(length, width):
        return length * width

    @classmethod
    def add_areas(cls, semicircle_radius, rectangle_length, rectangle_width):
        semicircle_area = cls.calculate_semicircle_area(semicircle_radius)
        rectangle_area = cls.calculate_rectangle_area(rectangle_length, rectangle_width)
        total_area = semicircle_area + rectangle_area
        return total_area

if __name__ == '__main__':
    result = AreaCalculator.add_areas(4, 5, 8)
    print(result)