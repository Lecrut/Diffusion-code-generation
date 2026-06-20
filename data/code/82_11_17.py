class YearCalculator:
    def __init__(self, year1: int, year2: int):
        self.year1 = year1
        self.year2 = year2

    def calculate_difference(self) -> int:
        return abs(self.year1 - self.year2)

if __name__ == '__main__':
    calculator_a = YearCalculator(2023, 1990)
    calculator_b = YearCalculator(2000, 2024)
    
    print(calculator_a.calculate_difference())
    print(calculator_b.calculate_difference())