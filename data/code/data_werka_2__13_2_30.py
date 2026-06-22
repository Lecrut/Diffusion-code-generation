from datetime import datetime

def parse_timestamps(timestamps):
    return [datetime.fromisoformat(ts) for ts in timestamps]

def find_extremes(datetime_objects):
    return min(datetime_objects), max(datetime_objects)

def calculate_total_elapsed_time(timestamps):
    if not timestamps:
        return 0
    datetime_objects = parse_timestamps(timestamps)
    earliest, latest = find_extremes(datetime_objects)
    total_elapsed_time = (latest - earliest).total_seconds()
    return total_elapsed_time

if __name__ == '__main__':
    sample_timestamps = [
        "2023-06-15T08:00:00Z",
        "2023-06-15T17:45:00Z",
        "2023-06-15T12:30:00Z"
    ]
    total_time = calculate_total_elapsed_time(sample_timestamps)
    print(total_time)