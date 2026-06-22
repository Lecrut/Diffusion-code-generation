from dateutil.relativedelta import relativedelta
from datetime import datetime

def days_remaining_in_month(year, month):
    if month == 12:
        next_year = year + 1
        next_month = 1
    else:
        next_year = year
        next_month = month + 1
    end_of_current_month = datetime(next_year, next_month, 1) - relativedelta(days=1)
    return end_of_current_month.day
if __name__ == '__main__':
    print(days_remaining_in_month(2023, 4))