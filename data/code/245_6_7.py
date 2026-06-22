class AreaCalculator:
    def __init__(self, diag1: int, diag2: int, side_length: int):
        self.diag1 = diag1
        self.diag2 = diag2
        self.side_length = side_length

    def calculate_rhombus_area(self) -> int:
        return (self.diag1 * self.diag2) // 4

    def calculate_square_area(self) -> int:
        return self.side_length ** 2

    def areas_equal(self) -> bool:
        area_rhombus = self.calculate_rhombus_area()
        area_square = self.calculate_square_area()
        return area_rhombus == area_square

if __name__ == '__main__':
    calculator = AreaCalculator(8, 6, 5)
    print(calculator.areas_equal())