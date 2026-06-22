class YearCalculator:
    def __init__(self, year: int):
        self.year = year

    def is_leap(self) -> bool:
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

    def days_in_year(self) -> int:
        return 366 if self.is_leap() else 365

    def total_seconds(self) -> int:
        return self.days_in_year() * 24 * 60 * 60

if __name__ == '__main__':
    calculator = YearCalculator(2023)
    print(calculator.days_in_year())
    print(calculator.total_seconds())