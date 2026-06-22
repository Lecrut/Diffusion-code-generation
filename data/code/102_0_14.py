import datetime

WEEKDAY_THRESHOLD = 5
DATE_FORMAT = "%Y-%m-%d"
EXPECTED_LENGTH = 10
SEPARATOR_POSITIONS = (4, 7)
SEPARATOR_CHAR = '-'

def is_weekday(date_string: str) -> bool:
    if not isinstance(date_string, str):
        raise ValueError("Input must be a string")
    if len(date_string) != EXPECTED_LENGTH:
        raise ValueError("Invalid date format: length mismatch")
    for pos in SEPARATOR_POSITIONS:
        if date_string[pos] != SEPARATOR_CHAR:
            raise ValueError("Invalid date format: missing separators")
    try:
        year = int(date_string[0:4])
        month = int(date_string[5:7])
        day = int(date_string[8:10])
        date_obj = datetime.date(year, month, day)
        return date_obj.weekday() < WEEKDAY_THRESHOLD
    except ValueError:
        raise ValueError(f"Invalid date format: {date_string}")

if __name__ == '__main__':
    test_cases = [
        "2023-10-07",
        "2023-10-08",
        "2023-02-29",
        "not-a-date",
        "2023-13-01"
    ]
    for date_str in test_cases:
        try:
            result = is_weekday(date_str)
            print(f"{date_str}: {result}")
        except ValueError as e:
            print(f"{date_str}: Error - {e}")