import datetime

def is_weekday(date_str: str) -> bool:
    try:
        parsed_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return parsed_date.weekday() < 5
    except ValueError:
        raise ValueError(f"Invalid date format: {date_str}")

if __name__ == '__main__':
    sample_dates = ["2023-10-07", "2023-10-08", "invalid-date", "2023-02-29"]
    for date in sample_dates:
        try:
            result = is_weekday(date)
            print(f"{date}: {result}")
        except ValueError as e:
            print(f"{date}: Error - {e}")