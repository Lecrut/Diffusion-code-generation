import calendar

def is_weekday(date_str: str) -> bool:
    year, month, day = map(int, date_str.split("-"))
    weekday = calendar.weekday(year, month, day)
    return weekday < 5

if __name__ == "__main__":
    sample_dates = ["2023-10-23", "2023-10-24", "2023-10-28"]
    for date in sample_dates:
        print(f"{date}: {is_weekday(date)}")