from dateutil.relativedelta import relativedelta
from datetime import datetime

def days_remaining_in_month(year, month):
    if month == 12:
        next_month = (year + 1, 1)
    else:
        next_month = (year, month + 1)
    first_day_of_next_month = datetime(next_month[0], next_month[1], 1)
    last_day_of_current_month = first_day_of_next_month - relativedelta(days=1)
    return last_day_of_current_month.day
if __name__ == '__main__':
    print(days_remaining_in_month(2023, 4))