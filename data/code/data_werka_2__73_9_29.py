from datetime import datetime, timedelta

class DateCalculator:
    def __init__(self, start_date: str, end_date: str):
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.strptime(end_date, '%Y-%m-%d')

    def get_days_difference(self) -> int:
        delta = self.end_date - self.start_date
        return delta.days

    def get_weeks_difference(self) -> int:
        return self.get_days_difference() // 7

    def get_start_date_obj(self) -> datetime:
        return self.start_date

if __name__ == '__main__':
    calc = DateCalculator('2020-01-01', '2021-06-15')
    days = calc.get_days_difference()
    weeks = calc.get_weeks_difference()
    start = calc.get_start_date_obj()
    print(days)
    print(weeks)
    print(start)