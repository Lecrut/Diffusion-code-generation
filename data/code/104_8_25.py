from datetime import datetime
from dateutil.relativedelta import relativedelta

TIME_UNITS = {
    'days': 0,
    'months': 0,
    'years': 0
}

def check_date_proximity(first_date, second_date):
    delta = relativedelta(first_date, second_date)
    TIME_UNITS['days'] = delta.days
    TIME_UNITS['months'] = delta.months
    TIME_UNITS['years'] = delta.years
    abs_days = abs(TIME_UNITS['days'])
    abs_months = abs(TIME_UNITS['months'])
    abs_years = abs(TIME_UNITS['years'])
    if abs_years > 0:
        return False
    if abs_months > 0:
        return False
    return abs_days <= 7

if __name__ == '__main__':
    date_a = datetime(2023, 10, 1, 12, 0, 0)
    date_b = datetime(2023, 10, 10, 12, 0, 0)
    result = check_date_proximity(date_a, date_b)
    print(result)