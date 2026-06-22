import calendar
from datetime import date

DAYS_IN_MONTH = {
    1: 31,
    2: 29 if (date.today().year % 4 == 0 and date.today().year % 100 != 0) or date.today().year % 400 == 0 else 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

class MonthDays:
    def remaining_days(self):
        today = date.today()
        return DAYS_IN_MONTH[today.month] - today.day

if __name__ == '__main__':
    month_days = MonthDays()
    print(month_days.remaining_days())