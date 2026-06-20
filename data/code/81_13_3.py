from datetime import datetime

def calculate_duration(start_time, end_time):
    start = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    duration = end - start
    return duration.total_seconds() / 3600

if __name__ == '__main__':
    print(calculate_duration("2023-10-01 12:00:00", "2023-10-01 14:30:00"))