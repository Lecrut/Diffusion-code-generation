import datetime

def is_valid_datetime(dt_str):
    try:
        datetime.datetime.strptime(dt_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def is_weekday(date_str):
    if not is_valid_datetime(date_str):
        raise ValueError("Invalid date format. Please provide a date in YYYY-MM-DD format.")
    
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    weekday = date_obj.weekday()
    return 0 <= weekday <= 4

if __name__ == '__main__':
    test_dates = [
        "2023-10-23",
        "2023-10-24",
        "2023-10-25",
        "2023-10-26",
        "2023-10-27",
        "2023-10-28",
        "2023-10-29"
    ]
    
    for date in test_dates:
        print(f"Date: {date}, Is Weekday: {is_weekday(date)}")