from datetime import datetime

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
SECONDS_PER_MINUTE = 60

def get_minutes_difference(start_str, end_str):
    start_dt = datetime.strptime(start_str, DATE_FORMAT)
    end_dt = datetime.strptime(end_str, DATE_FORMAT)
    delta = end_dt - start_dt
    total_seconds = delta.total_seconds()
    return total_seconds / SECONDS_PER_MINUTE

if __name__ == '__main__':
    t1 = '2023-01-01 10:00:00'
    t2 = '2023-01-01 12:30:00'
    diff = get_minutes_difference(t1, t2)
    print(diff)