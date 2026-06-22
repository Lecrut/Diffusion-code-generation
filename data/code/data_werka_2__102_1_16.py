import calendar

_WEEKDAY_THRESHOLD = 5
_DATE_FORMAT = "%Y-%m-%d"

def is_weekday(date_str: str) -> bool:
    year, month, day = map(int, date_str.split("-"))
    return calendar.weekday(year, month, day) < _WEEKDAY_THRESHOLD

if __name__ == "__main__":
    sample_dates = ["2024-01-15", "2024-01-20"]
    for date in sample_dates:
        print(f"{date}: {is_weekday(date)}")