from dateutil.relativedelta import relativedelta
from datetime import datetime

def days_remaining(year, month):
    current_date = datetime(year, month, 1)
    last_day_of_month = current_date + relativedelta(months=1) - relativedelta(days=1)
    return (last_day_of_month - current_date).days
if __name__ == '__main__':
    print(days_remaining(2023, 4))