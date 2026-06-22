from datetime import date, timedelta
WEEKEND_DAYS = {5, 6}

def is_weekend(dt: date) -> bool:
    return dt.weekday() in WEEKEND_DAYS

def is_weekend_in_range(start_date: date, end_date: date) -> bool:
    current_date = start_date
    while current_date <= end_date:
        if is_weekend(current_date):
            return True
        current_date += timedelta(days=1)
    return False
if __name__ == '__main__':
    print(is_weekend_in_range(date(2023, 4, 1), date(2023, 4, 7)))