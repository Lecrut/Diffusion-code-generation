from datetime import datetime

def validate_timestamps(timestamp1, timestamp2):
    if not isinstance(timestamp1, str) or not isinstance(timestamp2, str):
        raise ValueError("Both timestamps must be strings.")
    try:
        datetime.strptime(timestamp1, '%Y-%m-%d %H:%M:%S')
        datetime.strptime(timestamp2, '%Y-%m-%d %H:%M:%S')
    except ValueError as e:
        raise ValueError("Invalid timestamp format. Expected '%Y-%m-%d %H:%M:%S'.") from e

def calculate_time_difference(timestamp1, timestamp2):
    validate_timestamps(timestamp1, timestamp2)
    date1 = datetime.strptime(timestamp1, '%Y-%m-%d %H:%M:%S')
    date2 = datetime.strptime(timestamp2, '%Y-%m-%d %H:%M:%S')
    diff = abs(date2 - date1)
    hours = diff.seconds // 3600
    minutes = (diff.seconds // 60) % 60
    seconds = diff.seconds % 60
    return f"{hours}h {minutes}m {seconds}s"

if __name__ == '__main__':
    timestamp1 = "2023-01-15 12:00:00"
    timestamp2 = "2024-03-20 18:30:45"
    result = calculate_time_difference(timestamp1, timestamp2)
    print(f"Time difference between {timestamp1} and {timestamp2}: {result}")