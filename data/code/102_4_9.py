from datetime import datetime, date
from enum import IntEnum

class DayType(IntEnum):
    WEEKDAY = 0
    WEEKEND = 1

def check_timestamp_is_weekday(timestamp_value: str) -> bool:
    parsed_date = datetime.fromisoformat(timestamp_value).date()
    is_weekday_flag = parsed_date.weekday() < 5
    return bool(is_weekday_flag)

if __name__ == '__main__':
    test_date_string = "2024-05-18T14:30:00"
    outcome = check_timestamp_is_weekday(test_date_string)
    print(outcome)