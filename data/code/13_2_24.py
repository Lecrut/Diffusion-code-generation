from datetime import datetime

def calculate_total_elapsed_time(timestamps):
    if not timestamps:
        return 0
    
    earliest = min(datetime.fromisoformat(ts) for ts in timestamps)
    latest = max(datetime.fromisoformat(ts) for ts in timestamps)
    
    elapsed_time = latest - earliest
    return elapsed_time.total_seconds()

if __name__ == '__main__':
    sample_timestamps = [
        "2023-01-01T00:00:00Z",
        "2023-01-02T12:34:56Z",
        "2023-01-03T00:00:00Z"
    ]
    
    total_elapsed = calculate_total_elapsed_time(sample_timestamps)
    print(total_elapsed)