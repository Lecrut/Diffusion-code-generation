import datetime

def is_weekday(date_string: str) -> bool:
    try:
        parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
        return parsed_date.weekday() < 5
    except ValueError:
        raise ValueError(f"Invalid date format: {date_string}")

if __name__ == '__main__':
    sample_dates = ["2023-10-07", "2023-10-08", "invalid-date", "2023-02-29"]
    for date_str in sample_dates:
        try:
            result = is_weekday(date_str)
            print(f"{date_str}: {result}")
        except ValueError as e:
            print(f"{date_str}: Error - {e}")