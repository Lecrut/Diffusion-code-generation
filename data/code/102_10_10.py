import datetime

def is_weekday(date_obj):
    return 0 <= date_obj.weekday() < 5

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
        try:
            date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            print(f"{date_str} is a weekday: {is_weekday(date_obj)}")
        except ValueError:
            print(f"Invalid date format: {date_str}")