from datetime import datetime

def is_weekday(timestamp_str: str) -> bool:
    dt = datetime.fromisoformat(timestamp_str)
    return dt.weekday() < 5

if __name__ == '__main__':
    sample_timestamp = "2023-10-07T12:00:00"
    result = is_weekday(sample_timestamp)
    print(result)