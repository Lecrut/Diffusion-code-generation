from datetime import datetime
from enum import Enum
import sys

class DayCategory(Enum):
    WEEKDAY = "weekday"
    WEEKEND = "weekend"

def validate_timestamp_weekday(timestamp_input: str) -> DayCategory:
    try:
        parsed_dt = datetime.fromisoformat(timestamp_input)
    except (ValueError, TypeError) as e:
        raise ValueError(f"Invalid timestamp format: {timestamp_input}") from e
    
    weekday_index = parsed_dt.weekday()
    
    if weekday_index < 5:
        return DayCategory.WEEKDAY
    return DayCategory.WEEKEND

if __name__ == '__main__':
    test_ts = "2023-10-07T12:00:00"
    category = validate_timestamp_weekday(test_ts)
    print(category.value)