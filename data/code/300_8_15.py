from dateutil.relativedelta import relativedelta
from datetime import datetime

def remaining_days_in_month(date):
    next_month = date.replace(day=28) + relativedelta(days=4)
    return (next_month - next_month.replace(day=1)).days

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 15)
    print(remaining_days_in_month(sample_date))