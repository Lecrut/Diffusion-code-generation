from datetime import datetime

def duration_in_hours(timestamp1, timestamp2):
    dt1 = datetime.strptime(timestamp1, "%Y-%m-%d %H:%M:%S")
    dt2 = datetime.strptime(timestamp2, "%Y-%m-%d %H:%M:%S")
    delta = dt2 - dt1
    return delta.total_seconds() / 3600

if __name__ == '__main__':
    print(duration_in_hours("2023-10-01 12:00:00", "2023-10-01 14:30:00"))