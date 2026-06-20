from datetime import date
import calendar

def days_left_in_month():
    today = date.today()
    month_range = calendar.monthrange(today.year, today.month)
    return month_range[1] - today.day

if __name__ == '__main__':
    print(days_left_in_month())