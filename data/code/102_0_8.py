import datetime

WEEKDAY_LOOKUP = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

def is_weekday(date_string: str) -> bool:
    try:
        parsed_date = datetime.date.fromisoformat(date_string)
        return parsed_date.weekday() < 5
    except (ValueError, TypeError):
        raise ValueError(f"Invalid date format or type: {date_string}")

if __name__ == '__main__':
    sample_dates = ["2023-10-07", "2023-10-08", "2023-12-25", "invalid", "not-a-date"]
    for date_str in sample_dates:
        try:
            result = is_weekday(date_str)
            print(f"{date_str}: {result}")
        except ValueError as e:
            print(f"{date_str}: Error - {e}")