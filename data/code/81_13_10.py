from datetime import datetime

def calculate_duration_in_hours(timestamp1, timestamp2):
    dt1 = datetime.strptime(timestamp1, "%Y-%m-%d %H:%M:%S")
    dt2 = datetime.strptime(timestamp2, "%Y-%m-%d %H:%M:%S")
    duration = dt2 - dt1
    return duration.total_seconds() / 3600

if __name__ == '__main__':
    sample_timestamp1 = "2023-10-01 12:00:00"
    sample_timestamp2 = "2023-10-01 14:30:00"
    print(calculate_duration_in_hours(sample_timestamp1, sample_timestamp2))