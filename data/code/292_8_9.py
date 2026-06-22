class Parallelogram:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @staticmethod
    def calculate_perimeter(base, height):
        return 2 * (base + height)

if __name__ == '__main__':
    parallelogram_base = 10
    parallelogram_height = 5
    perimeter = Parallelogram.calculate_perimeter(parallelogram_base, parallelogram_height)
    print(f"Perimeter of parallelogram with base {parallelogram_base} and height {parallelogram_height}: {perimeter}")