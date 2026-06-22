from datetime import date
WEEKEND_DAYS = {5: True, 6: True}

def is_weekend(year, month, day):
    target_date = date(year, month, day)
    return WEEKEND_DAYS.get(target_date.weekday(), False)
if __name__ == '__main__':
    print(is_weekend(2023, 10, 7))
    print(is_weekend(2023, 10, 8))