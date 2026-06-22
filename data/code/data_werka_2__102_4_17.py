from datetime import datetime
from typing import Union

WEEKDAY_THRESHOLD: int = 5

def validate_timestamp_is_weekday(timestamp_input: Union[str, datetime]) -> bool:
    if isinstance(timestamp_input, str):
        parsed_dt: datetime = datetime.fromisoformat(timestamp_input)
    elif isinstance(timestamp_input, datetime):
        parsed_dt = timestamp_input
    else:
        raise ValueError("Unsupported input type")
    
    day_index: int = parsed_dt.weekday()
    return day_index < WEEKDAY_THRESHOLD

if __name__ == '__main__':
    sample_timestamp: str = "2023-10-07T12:00:00"
    computed_result: bool = validate_timestamp_is_weekday(sample_timestamp)
    print(computed_result)