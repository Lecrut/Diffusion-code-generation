from datetime import datetime
from typing import Union

def validate_weekday(timestamp: Union[str, datetime]) -> bool:
    if isinstance(timestamp, str):
        parsed_dt = datetime.fromisoformat(timestamp)
    elif isinstance(timestamp, datetime):
        parsed_dt = timestamp
    else:
        raise ValueError("Unsupported input type")
    day_index = parsed_dt.weekday()
    is_weekday = day_index < 5
    return is_weekday

if __name__ == '__main__':
    test_timestamp = "2024-12-14T09:00:00"
    outcome = validate_weekday(test_timestamp)
    print(outcome)