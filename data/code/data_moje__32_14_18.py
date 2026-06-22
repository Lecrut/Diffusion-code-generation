class RectangleAreaCalculator:
    DEFAULT_WIDTH = 12
    DEFAULT_HEIGHT = 7

    @staticmethod
    def compute_area(width, height):
        return width * height

    @classmethod
    def compute_with_defaults(cls):
        return cls.compute_area(cls.DEFAULT_WIDTH, cls.DEFAULT_HEIGHT)

if __name__ == '__main__':
    width_value = 8
    height_value = 15
    calculated_area = RectangleAreaCalculator.compute_area(width_value, height_value)
    print(calculated_area)