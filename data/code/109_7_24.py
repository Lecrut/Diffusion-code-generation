import calendar
import datetime

class MonthTimeCalculator:
    def __init__(self, reference_date=None):
        if reference_date is None:
            self.reference_date = datetime.datetime.now()
        else:
            self.reference_date = reference_date

    def get_seconds_remaining_in_current_month(self):
        year = self.reference_date.year
        month = self.reference_date.month
        last_day = calendar.monthrange(year, month)[1]
        next_month_first = datetime.datetime(year, month + 1 if month < 12 else 1, 1)
        if month == 12:
            next_month_first = datetime.datetime(year + 1, 1, 1)
        else:
            next_month_first = datetime.datetime(year, month + 1, 1)
        
        current_start = datetime.datetime(year, month, 1)
        total_seconds_in_month = int((next_month_first - current_start).total_seconds())
        
        seconds_elapsed = int((self.reference_date - current_start).total_seconds())
        remaining = total_seconds_in_month - seconds_elapsed
        return remaining

    def get_total_seconds_in_current_month(self):
        year = self.reference_date.year
        month = self.reference_date.month
        if month == 12:
            next_month_first = datetime.datetime(year + 1, 1, 1)
        else:
            next_month_first = datetime.datetime(year, month + 1, 1)
        current_start = datetime.datetime(year, month, 1)
        return int((next_month_first - current_start).total_seconds())

    def get_days_remaining_in_current_month(self):
        year = self.reference_date.year
        month = self.reference_date.month
        last_day = calendar.monthrange(year, month)[1]
        current_day = self.reference_date.day
        return last_day - current_day

if __name__ == '__main__':
    calc = MonthTimeCalculator(datetime.datetime(2023, 10, 15, 12, 30, 45))
    remaining = calc.get_seconds_remaining_in_current_month()
    total = calc.get_total_seconds_in_current_month()
    days_left = calc.get_days_remaining_in_current_month()
    print(remaining)
    print(total)
    print(days_left)