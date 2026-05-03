from datetime import datetime
def calculate_total_elapsed_time(timestamps):
    if not timestamps:
        return 0
    datetime_objects = [datetime.fromisoformat(ts) for ts in timestamps]
    earliest_time = min(datetime_objects)
    latest_time = max(datetime_objects)
    time_difference = latest_time - earliest_time
    return time_difference.total_seconds()
if __name__ == '__main__':
    sample_timestamps = [
        "2023-01-01T10:00:00",
        "2023-01-05T12:30:00",
        "2023-01-03T08:00:00"
    ]
    total_seconds = calculate_total_elapsed_time(sample_timestamps)
    print(total_seconds)