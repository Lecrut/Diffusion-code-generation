from datetime import date, timedelta

def calculate_next_seven_day_marker(start_date: date) -> date:
    if not isinstance(start_date, date):
        raise ValueError("start_date must be a date object")
    if start_date < date(1, 1, 1):
        raise ValueError("start_date must be a valid date")
    
    days_to_add = 7
    next_date = start_date + timedelta(days=days_to_add)
    return next_date

if __name__ == '__main__':
    start = date(2024, 1, 1)
    result = calculate_next_seven_day_marker(start)
    print(result)