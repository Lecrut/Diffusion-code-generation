from datetime import datetime, timedelta

def group_timestamps_by_hour(timestamps):
    buckets = {}
    for ts in timestamps:
        bucket_time = datetime.fromisoformat(ts).replace(minute=0, second=0, microsecond=0)
        if bucket_time not in buckets:
            buckets[bucket_time] = []
        buckets[bucket_time].append(ts)
    return buckets

if __name__ == '__main__':
    timestamps = [
        '2023-10-01T14:30:00',
        '2023-10-01T15:45:00',
        '2023-10-01T14:00:00',
        '2023-10-01T16:15:00'
    ]
    result = group_timestamps_by_hour(timestamps)
    print(result)