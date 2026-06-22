class Parallelogram:
    BASE = 10
    HEIGHT = 5

    @staticmethod
    def compute_area(base: float, height: float) -> float:
        return base * height

if __name__ == '__main__':
    result = Parallelogram.compute_area(Parallelogram.BASE, Parallelogram.HEIGHT)
    print(result)