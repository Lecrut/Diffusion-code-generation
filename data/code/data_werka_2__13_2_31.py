from datetime import datetime

def calculate_total_elapsed_time(timestamps):
    if not timestamps:
        return 0
    try:
        earliest = min(datetime.fromisoformat(ts) for ts in timestamps)
        latest = max(datetime.fromisoformat(ts) for ts in timestamps)
    except ValueError as e:
        raise ValueError("Invalid timestamp format") from e
    total_elapsed_time = (latest - earliest).total_seconds()
    return total_elapsed_time

if __name__ == '__main__':
    sample_timestamps = [
        "2023-10-05T08:00:00Z",
        "2023-10-05T17:45:00Z",
        "2023-10-05T12:20:00Z"
    ]
    total_time = calculate_total_elapsed_time(sample_timestamps)
    print(total_time)