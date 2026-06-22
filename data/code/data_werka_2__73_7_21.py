from datetime import datetime

SECONDS_PER_MINUTE = 60
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def get_minutes_difference(start_str, end_str):
    start_dt = datetime.strptime(start_str, DATE_FORMAT)
    end_dt = datetime.strptime(end_str, DATE_FORMAT)
    delta = end_dt - start_dt
    total_seconds = delta.total_seconds()
    return total_seconds / SECONDS_PER_MINUTE

if __name__ == '__main__':
    t1 = '2024-05-10 08:00:00'
    t2 = '2024-05-10 09:45:00'
    diff = get_minutes_difference(t1, t2)
    print(diff)