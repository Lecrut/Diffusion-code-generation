from datetime import datetime
from typing import Union

def is_weekday(timestamp: Union[str, datetime]) -> bool:
    if isinstance(timestamp, str):
        parsed_dt = datetime.fromisoformat(timestamp)
    elif isinstance(timestamp, datetime):
        parsed_dt = timestamp
    else:
        raise ValueError("Unsupported input type for timestamp")
    
    day_of_week = parsed_dt.weekday()
    return day_of_week < 5

if __name__ == '__main__':
    sample_timestamp = "2023-10-07T12:00:00"
    result = is_weekday(sample_timestamp)
    print(result)