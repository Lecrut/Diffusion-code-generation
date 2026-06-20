import datetime

def is_weekday(date_str):
    try:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        return date_obj.weekday() < 5
    except ValueError:
        return False

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