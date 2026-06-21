from datetime import datetime

def group_timestamps_by_hour(timestamps):
    buckets = {}
    for ts in timestamps:
        dt = datetime.fromisoformat(ts)
        hour_key = dt.strftime('%Y-%m-%d %H')
        if hour_key not in buckets:
            buckets[hour_key] = []
        buckets[hour_key].append(dt)
    return buckets

if __name__ == '__main__':
    sample_timestamps = [
        '2023-10-01T12:34:56',
        '2023-10-01T12:35:57',
        '2023-10-01T13:34:58',
        '2023-10-02T12:34:59'
    ]
    result = group_timestamps_by_hour(sample_timestamps)
    print(result)