from dateutil.relativedelta import relativedelta
from datetime import datetime

def days_remaining_in_month(date_str):
    input_date = datetime.strptime(date_str, '%Y-%m-%d')
    next_month = input_date + relativedelta(months=1)
    remaining_days = (next_month - input_date).days
    return remaining_days

if __name__ == '__main__':
    sample_date = '2023-04-15'
    print(days_remaining_in_month(sample_date))