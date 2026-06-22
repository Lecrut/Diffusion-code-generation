import calendar
from datetime import date

def get_days_left_in_month():
    today = date.today()
    _, num_days = calendar.monthrange(today.year, today.month)
    days_left = num_days - today.day
    return days_left

if __name__ == '__main__':
    sample_days_left = get_days_left_in_month()
    print(sample_days_left)