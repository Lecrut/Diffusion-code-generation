import datetime

def is_weekday(date_string: str) -> bool:
    if not isinstance(date_string, str):
        raise ValueError("Input must be a string")
    if len(date_string) != 10:
        raise ValueError("Invalid date format: length mismatch")
    if date_string[4] != '-' or date_string[7] != '-':
        raise ValueError("Invalid date format: missing separators")
    try:
        year = int(date_string[0:4])
        month = int(date_string[5:7])
        day = int(date_string[8:10])
        date_obj = datetime.date(year, month, day)
        return date_obj.weekday() < 5
    except ValueError:
        raise ValueError(f"Invalid date format: {date_string}")

if __name__ == '__main__':
    test_cases = [
        "2023-10-06",
        "2023-10-07",
        "2023-10-08",
        "2023-02-29",
        "not-a-date"
    ]
    for date_str in test_cases:
        try:
            result = is_weekday(date_str)
            print(f"{date_str}: {result}")
        except ValueError as e:
            print(f"{date_str}: Error - {e}")