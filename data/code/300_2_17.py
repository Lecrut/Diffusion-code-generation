from dateutil.relativedelta import relativedelta
from datetime import datetime

def days_remaining_in_month(year, month):
    if month < 1 or month > 12:
        raise ValueError('Month must be between 1 and 12')
    current_date = datetime(year, month, 1)
    next_month = (current_date + relativedelta(months=1)).replace(day=1)
    days_remaining = (next_month - current_date).days
    return days_remaining
if __name__ == '__main__':
    print(days_remaining_in_month(2023, 4))