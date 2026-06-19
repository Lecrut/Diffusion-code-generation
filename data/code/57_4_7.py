class Parallelogram:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return self.base * self.height

if __name__ == '__main__':
    parallelogram = Parallelogram(10, 5)
    area = parallelogram.calculate_area()
    print(f"Base: {parallelogram.base}")
    print(f"Height: {parallelogram.height}")
    print(f"Area: {area}")