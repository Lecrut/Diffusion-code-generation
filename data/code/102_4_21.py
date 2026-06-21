from datetime import datetime

def is_weekday(timestamp: str) -> bool:
    dt = datetime.fromisoformat(timestamp)
    return dt.weekday() < 5

if __name__ == '__main__':
    sample_timestamps = [
        "2023-10-23T10:00:00",
        "2023-10-28T10:00:00",
        "2023-10-29T10:00:00"
    ]
    for ts in sample_timestamps:
        result = is_weekday(ts)
        print(result)