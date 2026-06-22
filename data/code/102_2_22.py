from datetime import date

WEEKEND_DAYS = {5, 6}

def is_weekday(d: date) -> bool:
    if d.weekday() in WEEKEND_DAYS:
        return False
    return True

if __name__ == '__main__':
    test_date = date(2023, 10, 21)
    result = is_weekday(test_date)
    print(result)