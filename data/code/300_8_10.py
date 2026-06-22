from dateutil.relativedelta import relativedelta
from datetime import datetime

def days_remaining(year, month):
    current_date = datetime.now()
    target_date = datetime(year, month, 1)
    next_month = target_date + relativedelta(months=1)
    if target_date > current_date:
        return (next_month - target_date).days
    else:
        raise ValueError('Date is in the past')
if __name__ == '__main__':
    print(days_remaining(2023, 4))