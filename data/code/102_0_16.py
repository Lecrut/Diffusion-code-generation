import datetime

def is_valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def is_weekday(date_str):
    if not is_valid_date(date_str):
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'")
    
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

    for date_str in test_dates:
        result = is_weekday(date_str)
        print(f"Date: {date_str}, Is Weekday: {result}")