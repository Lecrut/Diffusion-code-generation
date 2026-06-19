class Parallelogram:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @staticmethod
    def calculate_area(base, height):
        return base * height

if __name__ == '__main__':
    base = 10
    height = 5
    parallelogram = Parallelogram(base, height)
    area = Parallelogram.calculate_area(parallelogram.base, parallelogram.height)
    print(area)