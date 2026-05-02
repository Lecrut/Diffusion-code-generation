import datetime
def calculate_total_elapsed_time(timestamps):
    if not timestamps:
        return None
    datetime_objects = [datetime.datetime.fromisoformat(ts) for ts in timestamps]
    earliest = min(datetime_objects)
    latest = max(datetime_objects)
    time_difference = latest - earliest
    return time_difference
if __name__ == '__main__':
    sample_timestamps = [
        "2023-01-01T10:00:00",
        "2023-01-05T12:30:00",
        "2023-01-03T08:00:00"
    ]
    elapsed_time = calculate_total_elapsed_time(sample_timestamps)
    if elapsed_time:
        print(elapsed_time)
    else:
        print("List of timestamps is empty")