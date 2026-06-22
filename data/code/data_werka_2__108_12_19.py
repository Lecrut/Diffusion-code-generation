from datetime import datetime

def extract_day_component(timestamp_str: str) -> int:
    try:
        parsed_dt = datetime.fromisoformat(timestamp_str)
    except ValueError as e:
        raise ValueError(f"Invalid ISO format: {timestamp_str}") from e
    return parsed_dt.day

if __name__ == '__main__':
    sample_timestamp = '2024-07-04T12:00:00'
    day_value = extract_day_component(sample_timestamp)
    print(day_value)