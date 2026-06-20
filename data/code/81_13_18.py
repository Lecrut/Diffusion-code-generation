from datetime import datetime

def duration_in_hours(timestamp1, timestamp2):
    dt1 = datetime.fromisoformat(timestamp1)
    dt2 = datetime.fromisoformat(timestamp2)
    delta = dt2 - dt1
    return delta.total_seconds() / 3600.0

if __name__ == '__main__':
    sample_timestamp1 = '2023-04-01T12:00:00'
    sample_timestamp2 = '2023-04-01T14:30:00'
    print(duration_in_hours(sample_timestamp1, sample_timestamp2))