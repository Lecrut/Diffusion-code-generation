class Parallelogram:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.base + self.height)

if __name__ == '__main__':
    parallelogram = Parallelogram(5, 3)
    perimeter = parallelogram.calculate_perimeter()
    print(f"Perimeter of parallelogram with base {parallelogram.base} and height {parallelogram.height}: {perimeter}")