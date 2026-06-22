import calendar
from datetime import date

def calculate_remaining_days(current_date):
    month = current_date.month
    year = current_date.year
    days_in_month = calendar.monthrange(year, month)[1]
    return days_in_month - current_date.day

if __name__ == '__main__':
    sample_date = date(2023, 10, 5)
    remaining_days = calculate_remaining_days(sample_date)
    print(remaining_days)