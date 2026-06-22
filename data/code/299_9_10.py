from datetime import date

def is_weekend_in_range(start_date: date, end_date: date) -> bool:
    if not isinstance(start_date, date) or not isinstance(end_date, date):
        raise ValueError("Both start_date and end_date must be of type date")
    if start_date > end_date:
        raise ValueError("start_date cannot be greater than end_date")
    
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() >= 5:
            return True
        current_date += timedelta(days=1)
    return False

if __name__ == '__main__':
    print(is_weekend_in_range(date(2023, 4, 1), date(2023, 4, 7)))