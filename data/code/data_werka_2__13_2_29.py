from datetime import datetime

def calculate_total_elapsed_time(timestamps):
    if not timestamps:
        raise ValueError('The list of timestamps cannot be empty.')
    datetime_objects = [datetime.fromisoformat(ts) for ts in timestamps]
    earliest = min(datetime_objects)
    latest = max(datetime_objects)
    total_elapsed_time = latest - earliest
    return total_elapsed_time
if __name__ == '__main__':
    sample_timestamps = ['2023-01-01T12:00:00Z', '2023-01-02T15:30:00Z', '2023-01-01T09:45:00Z']
    total_time = calculate_total_elapsed_time(sample_timestamps)
    print(total_time)