from datetime import datetime

def compute_duration_in_hours(start_time, end_time):
    start = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    duration = end - start
    return duration.total_seconds() / 3600

if __name__ == '__main__':
    sample_start = "2023-10-01 12:00:00"
    sample_end = "2023-10-01 14:30:00"
    print(compute_duration_in_hours(sample_start, sample_end))