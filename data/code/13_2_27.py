from datetime import datetime

def calculate_total_elapsed_time(timestamps):
    if not timestamps:
        return 0
    dt_objects = [datetime.fromisoformat(ts) for ts in timestamps]
    earliest = min(dt_objects)
    latest = max(dt_objects)
    total_elapsed_time = (latest - earliest).total_seconds()
    return total_elapsed_time
if __name__ == '__main__':
    sample_timestamps = ['2023-01-01T12:00:00Z', '2023-01-02T14:30:00Z', '2023-01-03T09:15:00Z']
    result = calculate_total_elapsed_time(sample_timestamps)
    print(result)