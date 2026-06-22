class YearDifferenceCalculator:
    def __init__(self, date1: str, date2: str):
        self.date1_str = date1
        self.date2_str = date2
        self.date1_year = int(date1[:4])
        self.date2_year = int(date2[:4])

    def compute_absolute_difference(self) -> int:
        return abs(self.date1_year - self.date2_year)

    def compute_signed_difference(self) -> int:
        return self.date1_year - self.date2_year

if __name__ == '__main__':
    calculator = YearDifferenceCalculator("2020-01-01", "2023-12-31")
    print(calculator.compute_absolute_difference())
    print(calculator.compute_signed_difference())