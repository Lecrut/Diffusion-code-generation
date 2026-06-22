from dateutil.relativedelta import relativedelta
from datetime import datetime

def days_remaining_in_month(year, month):
    if month == 12:
        next_month = (year + 1, 1)
    else:
        next_month = (year, month + 1)
    current_date = datetime(year, month, 1)
    next_month_first_day = datetime(*next_month)
    remaining_days = (next_month_first_day - current_date).days
    return remaining_days
if __name__ == '__main__':
    print(days_remaining_in_month(2023, 4))