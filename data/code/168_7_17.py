from datetime import datetime

def group_timestamps_into_buckets(timestamps):
    buckets = {}
    for ts in timestamps:
        dt = datetime.fromisoformat(ts)
        hour_key = dt.strftime('%Y-%m-%d %H')
        if hour_key not in buckets:
            buckets[hour_key] = []
        buckets[hour_key].append(ts)
    return buckets

if __name__ == '__main__':
    sample_timestamps = [
        '2023-10-01T14:30:00',
        '2023-10-01T15:45:00',
        '2023-10-01T14:35:00',
        '2023-10-02T14:30:00'
    ]
    print(group_timestamps_into_buckets(sample_timestamps))