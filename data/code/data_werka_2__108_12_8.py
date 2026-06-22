import datetime

def extract_day(timestamp_str: str) -> int:
    dt = datetime.datetime.fromisoformat(timestamp_str)
    return dt.day

if __name__ == '__main__':
    timestamp = '2024-07-04T12:00:00'
    day = extract_day(timestamp)
    print(day)