from dateutil.relativedelta import relativedelta
from datetime import datetime

def days_remaining(year, month):
    current_date = datetime.now()
    target_month = datetime(year, month + 1, 1) - relativedelta(days=1)
    remaining_days = (target_month - current_date).days
    return remaining_days
if __name__ == '__main__':
    print(days_remaining(2023, 4))