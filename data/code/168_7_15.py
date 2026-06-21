from datetime import datetime, timedelta
HOUR_DURATION = timedelta(hours=1)

def group_timestamps_by_hour(timestamps):
    buckets = {}
    for ts in timestamps:
        dt = datetime.fromisoformat(ts) if isinstance(ts, str) else ts
        hour_start = dt - timedelta(minutes=dt.minute, seconds=dt.second, microseconds=dt.microsecond)
        if hour_start not in buckets:
            buckets[hour_start] = []
        buckets[hour_start].append(dt)
    return buckets
if __name__ == '__main__':
    sample_timestamps = ['2023-10-01T14:30:00Z', '2023-10-01T15:15:00Z', '2023-10-01T16:45:00Z', '2023-10-01T17:00:00Z', '2023-10-01T18:30:00Z', '2023-10-01T19:55:00Z']
    grouped_timestamps = group_timestamps_by_hour(sample_timestamps)
    for bucket, timestamps in grouped_timestamps.items():
        print(f'{bucket}: {timestamps}')