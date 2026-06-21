from datetime import datetime

def group_timestamps_into_hourly_buckets(timestamps):
    buckets = {}
    for ts in timestamps:
        dt = datetime.strptime(ts, '%Y-%m-%d %H:%M:%S')
        hour_key = dt.strftime('%Y-%m-%d %H:00:00')
        if hour_key not in buckets:
            buckets[hour_key] = []
        buckets[hour_key].append(ts)
    return buckets

if __name__ == '__main__':
    timestamps = [
        '2023-10-01 14:30:00',
        '2023-10-01 15:45:00',
        '2023-10-01 16:00:00',
        '2023-10-02 14:30:00',
        '2023-10-02 14:45:00'
    ]
    result = group_timestamps_into_hourly_buckets(timestamps)
    print(result)