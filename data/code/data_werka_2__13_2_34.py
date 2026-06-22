from datetime import datetime

def calculate_total_elapsed_time(timestamps):
    if not timestamps:
        return 0
    datetime_objects = [datetime.fromisoformat(ts) for ts in timestamps]
    time_range = {'earliest': min(datetime_objects), 'latest': max(datetime_objects)}
    total_elapsed_time = (time_range['latest'] - time_range['earliest']).total_seconds()
    return total_elapsed_time
if __name__ == '__main__':
    sample_timestamps = ['2023-10-01T08:00:00Z', '2023-10-01T17:45:00Z', '2023-10-01T12:20:00Z']
    total_time = calculate_total_elapsed_time(sample_timestamps)
    print(total_time)