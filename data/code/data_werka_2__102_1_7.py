import calendar

def is_weekday(date_str):
    year, month, day = map(int, date_str.split("-"))
    weekday = calendar.weekday(year, month, day)
    return weekday < 5

if __name__ == "__main__":
    sample_dates = ["2023-10-07", "2023-10-08", "2023-10-09"]
    for date in sample_dates:
        print(f"{date}: {is_weekday(date)}")