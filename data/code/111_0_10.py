from datetime import date

class DateRangeCalculator:
    def __init__(self, start_year, start_month, start_day, end_year, end_month, end_day):
        self.start_date = date(start_year, start_month, start_day)
        self.end_date = date(end_year, end_month, end_day)

    def get_delta(self):
        return self.end_date - self.start_date

    def get_days(self):
        return self.get_delta().days

    def get_start(self):
        return self.start_date

    def get_end(self):
        return self.end_date

if __name__ == '__main__':
    calculator = DateRangeCalculator(2023, 1, 1, 2023, 12, 31)
    print(calculator.get_days())
    print(calculator.get_start())
    print(calculator.get_end())