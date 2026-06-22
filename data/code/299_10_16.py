from datetime import date
WEEKEND_DAYS = {5, 6}

def is_weekend(year, month, day):
    target_date = date(year, month, day)
    return target_date.weekday() in WEEKEND_DAYS
if __name__ == '__main__':
    print(is_weekend(2023, 10, 7))
    print(is_weekend(2023, 10, 8))