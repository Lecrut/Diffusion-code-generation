from datetime import date

class DateDifferenceCalculator:
    def __init__(self, start_date: str, end_date: str):
        self.start_date = date.fromisoformat(start_date)
        self.end_date = date.fromisoformat(end_date)

    def calculate_difference(self) -> int:
        return abs((self.end_date - self.start_date).days)

if __name__ == '__main__':
    calculator = DateDifferenceCalculator("2023-01-15", "2021-11-20")
    print(f"Date Difference in Days: {calculator.calculate_difference()}")