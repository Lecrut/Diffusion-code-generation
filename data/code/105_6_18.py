from datetime import date, timedelta

DAYS_PER_WEEK = 7
START_YEAR = 2024
START_MONTH = 1
START_DAY = 1

def get_next_multiple_of_7_days():
    start_date = date(START_YEAR, START_MONTH, START_DAY)
    offset = DAYS_PER_WEEK
    next_date = start_date + timedelta(days=offset)
    return next_date

if __name__ == '__main__':
    result = get_next_multiple_of_7_days()
    print(result)