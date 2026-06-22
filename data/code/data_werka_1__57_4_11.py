class Parallelogram:

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return self.base * self.height
if __name__ == '__main__':
    base = 8
    height = 5
    parallelogram = Parallelogram(base, height)
    area = parallelogram.calculate_area()
    print(f'Base: {base}')
    print(f'Height: {height}')
    print(f'Area of the parallelogram: {area}')