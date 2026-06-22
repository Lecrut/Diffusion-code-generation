from datetime import datetime

def calculate_total_minutes_between(start_str, end_str):
    fmt = '%Y-%m-%d %H:%M:%S'
    try:
        start_dt = datetime.strptime(start_str, fmt)
        end_dt = datetime.strptime(end_str, fmt)
    except ValueError as e:
        raise ValueError(f"Invalid date string format: {e}")
    delta = end_dt - start_dt
    total_seconds = delta.total_seconds()
    return total_seconds / 60.0

if __name__ == '__main__':
    t1 = '2024-05-10 08:15:30'
    t2 = '2024-05-10 10:45:30'
    minutes_diff = calculate_total_minutes_between(t1, t2)
    print(minutes_diff)