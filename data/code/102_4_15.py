from datetime import datetime

def is_weekday(timestamp: str) -> bool:
    dt = datetime.fromisoformat(timestamp)
    return 0 <= dt.weekday() <= 4

if __name__ == '__main__':
    sample_timestamp = '2023-10-07T12:00:00'
    result = is_weekday(sample_timestamp)
    print(result)