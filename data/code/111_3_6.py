from datetime import date
from dateutil.relativedelta import relativedelta

def subtract_months(d, n):
    return d - relativedelta(months=n)

if __name__ == '__main__':
    original_date = date(2023, 10, 15)
    result = subtract_months(original_date, 3)
    print(result)