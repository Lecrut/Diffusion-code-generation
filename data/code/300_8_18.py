from dateutil.relativedelta import relativedelta
from datetime import datetime

def remaining_days_in_month(date):
    next_month = date + relativedelta(months=1)
    first_day_of_next_month = next_month.replace(day=1)
    return (first_day_of_next_month - date).days

if __name__ == '__main__':
    sample_date = datetime(2023, 4, 15)
    print(remaining_days_in_month(sample_date))