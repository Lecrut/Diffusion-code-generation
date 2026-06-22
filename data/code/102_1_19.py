import calendar

def check_weekday(date_str):
    year, month, day = map(int, date_str.split("-"))
    weekday = calendar.weekday(year, month, day)
    return weekday < 5

if __name__ == "__main__":
    dates = ["2023-10-01", "2023-10-02", "2023-10-07"]
    for date in dates:
        is_weekday = check_weekday(date)
        print(f"{date}: {is_weekday}")