import datetime

WEEKDAY_THRESHOLD = 5

def check_is_weekday(target_date):
    if isinstance(target_date, str):
        try:
            parsed = datetime.datetime.strptime(target_date, "%Y-%m-%d").date()
        except ValueError as err:
            raise ValueError(f"Failed to parse date string: {target_date}") from err
    elif isinstance(target_date, datetime.date):
        parsed = target_date
    else:
        raise ValueError(f"Expected date or string, got {type(target_date)}")
    return parsed.weekday() < WEEKDAY_THRESHOLD

if __name__ == '__main__':
    test_date = "2023-10-23"
    is_week = check_is_weekday(test_date)
    print(is_week)