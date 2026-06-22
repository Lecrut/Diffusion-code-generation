from datetime import date, timedelta
weekend_days = {5: True, 6: True}

def is_weekend_in_range(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() in weekend_days:
            return True
        current_date += timedelta(days=1)
    return False
if __name__ == '__main__':
    print(is_weekend_in_range(date(2023, 4, 1), date(2023, 4, 7)))