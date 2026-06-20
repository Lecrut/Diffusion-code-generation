import datetime

class DateCalculator:
    def days_between(self, date1: datetime.date, date2: datetime.date) -> int:
        return abs((date2 - date1).days)

if __name__ == '__main__':
    calculator = DateCalculator()
    date_a = datetime.date(2023, 1, 1)
    date_b = datetime.date(2023, 1, 10)
    result1 = calculator.days_between(date_a, date_b)
    print(result1)

    date_c = datetime.date(2024, 12, 31)
    date_d = datetime.date(2025, 1, 1)
    result2 = calculator.days_between(date_c, date_d)
    print(result2)