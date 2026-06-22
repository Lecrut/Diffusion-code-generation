from dateutil.relativedelta import relativedelta
from datetime import datetime

def days_remaining(year, month):
    current_date = datetime.now()
    target_date = datetime(year, month + 1, 1)
    difference = relativedelta(target_date, current_date)
    return difference.days

if __name__ == '__main__':
    print(days_remaining(2023, 4))