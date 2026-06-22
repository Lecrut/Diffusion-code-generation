from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

WEEK_DAYS = 7

def is_close_enough(target: datetime, reference: datetime) -> bool:
    delta = relativedelta(target, reference)
    abs_days = abs(delta.days)
    abs_months = abs(delta.months)
    abs_years = abs(delta.years)
    if abs_months != 0 or abs_years != 0:
        return False
    return abs_days <= WEEK_DAYS

if __name__ == '__main__':
    start_date = datetime(2023, 11, 1, 10, 30, 0)
    end_date = datetime(2023, 11, 8, 10, 30, 0)
    result = is_close_enough(start_date, end_date)
    print(result)