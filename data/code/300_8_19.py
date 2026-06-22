from datetime import date
from dateutil.relativedelta import relativedelta

def remaining_days_in_month(year, month):
    if 1 <= month <= 12:
        next_month = month % 12 + 1
        next_year = year + (month == 12)
        last_day_of_current_month = date(year, month, 1) + relativedelta(months=1) - relativedelta(days=1)
        return (last_day_of_current_month - date(year, month, 1)).days + 1
    else:
        raise ValueError('Invalid month')
if __name__ == '__main__':
    print(remaining_days_in_month(2023, 4))