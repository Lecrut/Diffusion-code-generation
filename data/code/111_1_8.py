import datetime

def add_days_to_date(date_obj, days):
    if not isinstance(date_obj, datetime.date) or not isinstance(days, int):
        raise ValueError("Invalid input: date_obj must be a datetime.date object and days must be an integer.")
    
    return date_obj + datetime.timedelta(days=days)

if __name__ == '__main__':
    date1 = datetime.date(2024, 7, 4)
    result1 = add_days_to_date(date1, 30)
    print(f"Original: {date1}, Result: {result1}")