from datetime import datetime

def calculate_total_elapsed_time(timestamps):
    if not timestamps:
        return 0
    datetime_objects = [datetime.fromisoformat(ts) for ts in timestamps]
    earliest = min(datetime_objects)
    latest = max(datetime_objects)
    elapsed_time = (latest - earliest).total_seconds()
    return elapsed_time
if __name__ == '__main__':
    sample_timestamps = ['2023-01-01T12:00:00Z', '2023-01-02T14:30:00Z', '2023-01-01T09:45:00Z']
    total_elapsed_time = calculate_total_elapsed_time(sample_timestamps)
    print(total_elapsed_time)