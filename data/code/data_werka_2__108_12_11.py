from datetime import datetime

def get_day_component(timestamp_str: str) -> int:
    if not isinstance(timestamp_str, str):
        raise ValueError("Input must be a string")
    dt = datetime.fromisoformat(timestamp_str)
    return dt.day

if __name__ == '__main__':
    sample_timestamp = '2024-07-04T12:00:00'
    day_value = get_day_component(sample_timestamp)
    print(day_value)