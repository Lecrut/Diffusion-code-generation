from datetime import datetime

def is_timestamp_on_weekday(timestamp: str) -> bool:
    try:
        dt = datetime.fromisoformat(timestamp)
        return dt.weekday() < 5
    except (ValueError, TypeError) as e:
        raise ValueError(f"Invalid timestamp format: {timestamp}") from e

if __name__ == '__main__':
    test_timestamp = '2023-10-07T12:00:00'
    is_weekday = is_timestamp_on_weekday(test_timestamp)
    print(is_weekday)