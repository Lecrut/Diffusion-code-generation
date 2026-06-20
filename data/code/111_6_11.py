from datetime import date, timedelta

def is_weekday(date):
    return date.weekday() < 5

def find_next_monday(start_date):
    if not is_weekday(start_date):
        raise ValueError("Start date must be a weekday.")
    
    days_to_add = (7 - start_date.weekday()) % 7
    next_monday = start_date + timedelta(days=days_to_add)
    return next_monday

if __name__ == '__main__':
    sample_date = date(2023, 9, 10)
    result = find_next_monday(sample_date)
    print(f"Next Monday after {sample_date}: {result}")