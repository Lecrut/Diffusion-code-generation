class BoxSurfaceAreaCalculator:
    DIMENSIONS = (10, 8, 6)

    @staticmethod
    def compute(length, width, height):
        return 2 * (length * width + width * height + height * length)

    @classmethod
    def get_surface_area(cls):
        length, width, height = cls.DIMENSIONS
        return cls.compute(length, width, height)

if __name__ == '__main__':
    result = BoxSurfaceAreaCalculator.get_surface_area()
    print(result)