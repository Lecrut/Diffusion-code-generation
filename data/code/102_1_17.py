import calendar

def is_weekday(date_str: str) -> bool:
    year, month, day = map(int, date_str.split("-"))
    return calendar.weekday(year, month, day) < 5

if __name__ == "__main__":
    sample_dates = ["2023-10-01", "2023-10-02", "2023-10-07"]
    for date in sample_dates:
        print(f"{date}: {is_weekday(date)}")