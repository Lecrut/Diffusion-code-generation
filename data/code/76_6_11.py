from datetime import date, timedelta

class DateDifferenceCalculator:
    def __init__(self, date_str1: str, date_str2: str):
        self.date_format = "%Y-%m-%d"
        self.date1 = date.fromisoformat(date_str1)
        self.date2 = date.fromisoformat(date_str2)

    def calculate_difference(self) -> int:
        delta = abs(self.date2 - self.date1)
        return delta.days

if __name__ == '__main__':
    sample_date_str1 = "2023-01-01"
    sample_date_str2 = "2023-12-31"
    calculator = DateDifferenceCalculator(sample_date_str1, sample_date_str2)
    difference = calculator.calculate_difference()
    print(f"The number of days between {sample_date_str1} and {sample_date_str2} is: {difference}")