from datetime import date
from dateutil.relativedelta import relativedelta
from dateutil.rrule import rrule, MONTHLY, MO, TU, WE, TH, FR, SA, SU

def next_fifteenth_following(start_date: date) -> date:
    if start_date.day >= 15:
        next_month = start_date + relativedelta(months=1)
        return date(next_month.year, next_month.month, 15)
    else:
        return date(start_date.year, start_date.month, 15)
if __name__ == '__main__':
    start_date = date(2023, 3, 3)
    result = next_fifteenth_following(start_date)
    print(result)