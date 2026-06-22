class Parallelogram:
    @staticmethod
    def compute_area(base, height):
        return float(base * height)

if __name__ == '__main__':
    base = 12.5
    height = 8.0
    area = Parallelogram.compute_area(base, height)
    print(area)