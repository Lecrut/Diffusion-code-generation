class Parallelogram:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @staticmethod
    def calculate_area(base, height):
        return base * height

if __name__ == '__main__':
    base_value = 8.0
    height_value = 5.0
    parallelogram = Parallelogram(base_value, height_value)
    area = parallelogram.calculate_area(parallelogram.base, parallelogram.height)
    print(area)