from datetime import date

class DateDiffCalculator:
    def __init__(self, start: date, end: date):
        self.start = start
        self.end = end

    def calculate_years(self) -> int:
        years = self.end.year - self.start.year
        if (self.end.month, self.end.day) < (self.start.month, self.start.day):
            years -= 1
        return years

    def calculate_days(self) -> int:
        delta = self.end - self.start
        return delta.days

    def get_summary(self) -> dict:
        return {
            "start": self.start,
            "end": self.end,
            "years": self.calculate_years(),
            "days": self.calculate_days()
        }

if __name__ == '__main__':
    start_date = date(1990, 5, 15)
    end_date = date(2023, 8, 20)
    calculator = DateDiffCalculator(start_date, end_date)
    print(calculator.calculate_years())
    print(calculator.calculate_days())
    print(calculator.get_summary())