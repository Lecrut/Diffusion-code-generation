import datetime

def is_weekday(timestamp: str) -> bool:
    dt = datetime.datetime.fromisoformat(timestamp)
    return dt.weekday() < 5

if __name__ == '__main__':
    sample_timestamps = [
        "2023-10-02T10:00:00",
        "2023-10-07T10:00:00",
        "2023-10-08T10:00:00"
    ]
    for ts in sample_timestamps:
        result = is_weekday(ts)
        print(result)