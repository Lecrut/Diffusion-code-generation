from datetime import datetime

def compute_minutes_difference(first_date_str, second_date_str):
    date_format = '%Y-%m-%d %H:%M:%S'
    try:
        first_dt = datetime.strptime(first_date_str, date_format)
        second_dt = datetime.strptime(second_date_str, date_format)
    except ValueError as e:
        raise ValueError(f"Invalid date format: {e}")
    time_delta = second_dt - first_dt
    total_seconds = time_delta.total_seconds()
    minutes = total_seconds / 60
    return minutes

if __name__ == '__main__':
    start = '2023-01-01 10:00:00'
    end = '2023-01-01 12:30:00'
    diff = compute_minutes_difference(start, end)
    print(diff)