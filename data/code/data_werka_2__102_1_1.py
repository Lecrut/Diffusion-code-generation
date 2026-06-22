import calendar

def is_weekday(date_str: str) -> bool:
    year, month, day = map(int, date_str.split("-"))
    weekday = calendar.weekday(year, month, day)
    return weekday < 5

if __name__ == "__main__":
    sample_dates = ["2023-10-02", "2023-10-07"]
    results = [is_weekday(d) for d in sample_dates]
    print(results)