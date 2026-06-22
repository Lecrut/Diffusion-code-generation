from datetime import datetime
from typing import Any

WEEKDAY_COUNT = 5

def is_weekday(date_string: str) -> bool:
    parsed_date = datetime.fromisoformat(date_string)
    weekday_index = parsed_date.weekday()
    is_weekday_flag = weekday_index < WEEKDAY_COUNT
    return is_weekday_flag

if __name__ == '__main__':
    test_input = "2024-02-10"
    output = is_weekday(test_input)
    print(output)