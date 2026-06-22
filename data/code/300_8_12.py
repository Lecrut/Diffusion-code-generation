from dateutil.relativedelta import relativedelta
from datetime import datetime

def days_remaining_in_month(date_str):
    input_date = datetime.strptime(date_str, '%Y-%m-%d')
    next_month_first_day = input_date.replace(day=1) + relativedelta(months=1)
    remaining_days = (next_month_first_day - input_date).days
    return remaining_days

if __name__ == '__main__':
    print(days_remaining_in_month('2023-04-15'))