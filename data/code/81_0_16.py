from datetime import datetime

def parse_time(time_str: str) -> datetime:
    try:
        return datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    except ValueError as e:
        raise ValueError(f"Invalid time format. Please use 'YYYY-MM-DD HH:MM:SS': {e}")

def calculate_elapsed_hours(start_time_str: str, end_time_str: str) -> float:
    start_time = parse_time(start_time_str)
    end_time = parse_time(end_time_str)
    time_difference = end_time - start_time
    elapsed_seconds = time_difference.total_seconds()
    elapsed_hours = elapsed_seconds / 3600.0
    return elapsed_hours

if __name__ == '__main__':
    start = "2023-10-27 09:00:00"
    end = "2023-10-27 17:30:00"
    result = calculate_elapsed_hours(start, end)
    print(result)