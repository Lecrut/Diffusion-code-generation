from datetime import date
from dateutil.relativedelta import relativedelta

def subtract_months(target_date, months):
    return target_date - relativedelta(months=months)

if __name__ == '__main__':
    start_date = date(2023, 10, 15)
    result = subtract_months(start_date, 3)
    print(result)