from datetime import datetime

def is_weekday(timestamp: str) -> bool:
    try:
        dt = datetime.fromisoformat(timestamp)
    except (TypeError, ValueError):
        raise ValueError(f"Invalid timestamp format: {timestamp}")
    
    weekday_mask = dt.weekday()
    return weekday_mask < 5

if __name__ == '__main__':
    test_timestamp = "2023-10-07T12:00:00"
    is_weekday_result = is_weekday(test_timestamp)
    print(is_weekday_result)