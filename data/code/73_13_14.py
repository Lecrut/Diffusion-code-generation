from datetime import datetime

def time_difference_in_seconds(timestamp1: str, timestamp2: str) -> int:
    dt1 = datetime.fromisoformat(timestamp1)
    dt2 = datetime.fromisoformat(timestamp2)
    return abs((dt2 - dt1).total_seconds())

if __name__ == '__main__':
    sample_timestamp1 = '2023-04-01T12:00:00+00:00'
    sample_timestamp2 = '2023-04-01T12:05:00+00:00'
    print(time_difference_in_seconds(sample_timestamp1, sample_timestamp2))