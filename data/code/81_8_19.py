from datetime import datetime

def validate_time_format(time_str):
    try:
        return datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S%z')
    except ValueError:
        raise ValueError("Time string must be in 'YYYY-MM-DD HH:MM:SS+HH:MM' format")

def calculate_elapsed_hours(start_time, end_time):
    if start_time > end_time:
        end_time += timedelta(days=1)
    return (end_time - start_time).total_seconds() / 3600

if __name__ == '__main__':
    try:
        start = validate_time_format('2023-10-01 14:00:00+02:00')
        end = validate_time_format('2023-10-01 16:30:00+02:00')
        elapsed_hours = calculate_elapsed_hours(start, end)
        print(f"Elapsed time in hours: {elapsed_hours:.2f}")
    except ValueError as e:
        print(e)