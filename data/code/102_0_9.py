import datetime

def is_weekday(date_str):
    try:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        return date_obj.weekday() < 5
    except ValueError:
        return False

if __name__ == '__main__':
    sample_dates = [
        "2023-11-01",
        "2023-11-02",
        "2023-11-03",
        "2023-11-04",
        "2023-11-05",
        "2023-11-06",
        "2023-11-07"
    ]

    for date_str in sample_dates:
        result = is_weekday(date_str)
        print(f"Date: {date_str}, Is Weekday: {result}")