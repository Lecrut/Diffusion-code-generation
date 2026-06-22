from datetime import datetime
import calendar

DATE_INPUT_FORMAT = '%Y-%m-%d'
DAYS_IN_WEEK = 7

def get_days_between(date_a: str, date_b: str) -> int:
    dt_a = datetime.strptime(date_a, DATE_INPUT_FORMAT)
    dt_b = datetime.strptime(date_b, DATE_INPUT_FORMAT)
    delta = dt_b - dt_a
    return abs(delta.days)

if __name__ == '__main__':
    start = '2021-05-15'
    end = '2022-01-10'
    days = get_days_between(start, end)
    print(days)