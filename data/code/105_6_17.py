import datetime

class DateCalculator:
    def __init__(self, start_date):
        self.start_date = start_date

    def nth_day_after(self, n):
        if n < 0:
            raise ValueError("N must be a non-negative integer")
        target_date = self.start_date + datetime.timedelta(days=n)
        return target_date

if __name__ == '__main__':
    calculator = DateCalculator(datetime.date(2024, 1, 1))
    result1 = calculator.nth_day_after(7)
    print(f"Result after 7 days: {result1}")
    result2 = calculator.nth_day_after(14)
    print(f"Result after 14 days: {result2}")
    result3 = calculator.nth_day_after(21)
    print(f"Result after 21 days: {result3}")