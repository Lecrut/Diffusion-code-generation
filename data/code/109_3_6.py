import calendar
from datetime import date

def days_left_in_month():
    today = date.today()
    _, last_day = calendar.monthrange(today.year, today.month)
    return last_day - today.day

if __name__ == '__main__':
    print(days_left_in_month())