from datetime import datetime

def extract_day_component(timestamp_str: str) -> int:
    if not isinstance(timestamp_str, str):
        raise ValueError("Input must be a string")
    if not timestamp_str:
        raise ValueError("Input string cannot be empty")
    try:
        dt_object = datetime.fromisoformat(timestamp_str)
    except ValueError as err:
        raise ValueError(f"Failed to parse timestamp: {timestamp_str}") from err
    return dt_object.day

if __name__ == '__main__':
    sample_timestamp = '2024-07-04T12:00:00'
    result = extract_day_component(sample_timestamp)
    print(result)