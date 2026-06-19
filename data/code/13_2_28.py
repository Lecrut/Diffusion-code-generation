from datetime import datetime

def calculate_total_elapsed_time(timestamps):
    if not timestamps:
        return 0
    datetimes = [datetime.fromisoformat(ts) for ts in timestamps]
    earliest = min(datetimes)
    latest = max(datetimes)
    total_elapsed_time = (latest - earliest).total_seconds()
    return total_elapsed_time
if __name__ == '__main__':
    sample_timestamps = ['2023-10-01T12:00:00', '2023-10-01T14:30:00', '2023-10-01T09:15:00', '2023-10-01T16:45:00']
    total_time = calculate_total_elapsed_time(sample_timestamps)
    print(total_time)