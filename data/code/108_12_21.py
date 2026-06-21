from datetime import datetime
from typing import Tuple

def _validate_iso_format(timestamp: str) -> str:
    try:
        datetime.fromisoformat(timestamp)
    except ValueError:
        raise ValueError(f"Invalid ISO format string: {timestamp}")
    return timestamp

def extract_day_component(timestamp: str) -> int:
    validated_ts = _validate_iso_format(timestamp)
    dt_object = datetime.fromisoformat(validated_ts)
    return dt_object.day

if __name__ == '__main__':
    input_timestamp = '2024-07-04T12:00:00'
    result = extract_day_component(input_timestamp)
    print(result)