import calendar
from datetime import datetime

class DaysLeftInMonth:
    def days_left(self):
        today = datetime.now()
        _, num_days = calendar.monthrange(today.year, today.month)
        return num_days - today.day

if __name__ == '__main__':
    dl = DaysLeftInMonth()
    print(dl.days_left())