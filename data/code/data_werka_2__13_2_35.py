from datetime import datetime

def calculate_total_elapsed_time(timestamps):
    if not timestamps:
        return 0
    
    try:
        datetime_objects = [datetime.fromisoformat(ts) for ts in timestamps]
    except ValueError as e:
        raise ValueError("Invalid timestamp format") from e
    
    earliest = min(datetime_objects)
    latest = max(datetime_objects)
    
    elapsed_time = (latest - earliest).total_seconds()
    return elapsed_time

if __name__ == '__main__':
    sample_timestamps = [
        "2023-09-15T08:00:00Z",
        "2023-09-16T17:45:00Z",
        "2023-09-15T14:15:00Z"
    ]
    total_time = calculate_total_elapsed_time(sample_timestamps)
    print(total_time)