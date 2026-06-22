from datetime import datetime
import re

def extract_day_component(timestamp_str: str) -> int:
    if not isinstance(timestamp_str, str):
        raise ValueError("Input must be a string")
    pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$'
    if not re.match(pattern, timestamp_str):
        raise ValueError(f"Invalid timestamp format: {timestamp_str}")
    dt = datetime.fromisoformat(timestamp_str)
    return dt.day

if __name__ == '__main__':
    sample_timestamp = '2024-07-04T12:00:00'
    day_value = extract_day_component(sample_timestamp)
    print(day_value)