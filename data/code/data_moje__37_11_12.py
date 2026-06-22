class Parallelogram:
    BASE = 8.0
    HEIGHT = 4.5

    @staticmethod
    def compute_area(base, height):
        return base * height

if __name__ == '__main__':
    area = Parallelogram.compute_area(Parallelogram.BASE, Parallelogram.HEIGHT)
    print(area)