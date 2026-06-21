from datetime import date

class MonthCalculator:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def get_remaining_days(self):
        delta = self.end_date - self.start_date
        return delta.days

    def get_total_days(self):
        return self.end_date.day

if __name__ == '__main__':
    start = date(2023, 11, 10)
    end = date(2023, 11, 30)
    calc = MonthCalculator(start, end)
    print(calc.get_remaining_days())
    print(calc.get_total_days())