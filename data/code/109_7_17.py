import datetime

class TimeRemainingCalculator:
    def __init__(self, current_date):
        self.current_date = current_date
    
    def get_days_remaining_in_current_month(self):
        next_month = (self.current_date.replace(day=28) + datetime.timedelta(days=4)).replace(day=1)
        if self.current_date.month == 12:
            next_month = self.current_date.replace(year=self.current_date.year + 1, month=1, day=1)
        else:
            next_month = self.current_date.replace(month=self.current_date.month + 1, day=1)
        days_in_current_month = (next_month - self.current_date).days
        return days_in_current_month

if __name__ == '__main__':
    current_date = datetime.date(2024, 2, 10)
    calculator = TimeRemainingCalculator(current_date)
    remaining_days = calculator.get_days_remaining_in_current_month()
    print(f"Days remaining in the current month: {remaining_days}")