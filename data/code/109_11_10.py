import datetime

class TimeRemainingCalculator:
    def __init__(self, target_month, target_day):
        self.target_date = datetime.date(datetime.date.today().year, target_month, target_day)

    def calculate_time_remaining(self):
        today = datetime.date.today()
        if self.target_date >= today:
            remaining_days = (self.target_date - today).days
            hours = remaining_days * 24
            minutes = hours * 60
            seconds = minutes * 60
            return f"{hours} hours, {minutes} minutes, {seconds} seconds"
        else:
            return "Target date has already passed"

if __name__ == '__main__':
    calculator_1 = TimeRemainingCalculator(10, 25)
    print(calculator_1.calculate_time_remaining())