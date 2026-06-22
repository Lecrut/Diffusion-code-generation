class ParallelogramCalculator:
    BASE = 7
    HEIGHT = 4

    @staticmethod
    def compute_area(b, h):
        return b * h

    @classmethod
    def run_example(cls):
        return cls.compute_area(cls.BASE, cls.HEIGHT)

if __name__ == '__main__':
    print(ParallelogramCalculator.run_example())