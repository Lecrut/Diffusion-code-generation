import datetime

def contains_weekdays(date_strings):
    weekday_check = [datetime.datetime.strptime(date_str, "%Y-%m-%d").weekday() < 5 for date_str in date_strings]
    return any(weekday_check)

if __name__ == '__main__':
    dates = ["2023-10-27", "2024-02-29", "2023-10-28", "2023-02-28"]
    print(f"Contains weekdays: {contains_weekdays(dates)}")