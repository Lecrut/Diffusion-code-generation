class SquareCalculator:
    def __init__(self):
        self._samples = [4, 6, 9]

    def calculate_area(self, side_length):
        if side_length < 0:
            raise ValueError("Side length cannot be negative")
        return side_length ** 2

    def print_areas(self):
        for sample in self._samples:
            area = self.calculate_area(sample)
            print(f"The area of a square with side length {sample} is {area}")

if __name__ == '__main__':
    calculator = SquareCalculator()
    calculator.print_areas()