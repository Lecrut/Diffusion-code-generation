from datetime import date

def is_weekend_in_range(start_date: date, end_date: date) -> bool:
    if start_date > end_date:
        raise ValueError("Start date must be before or equal to end date.")
    
    for current_date in range(start_date.toordinal(), end_date.toordinal() + 1):
        if date.fromordinal(current_date).weekday() >= 5:
            return True
    return False

if __name__ == '__main__':
    try:
        start = date(2023, 4, 1)
        end = date(2023, 4, 7)
        print(is_weekend_in_range(start, end))
    except ValueError as e:
        print(e)