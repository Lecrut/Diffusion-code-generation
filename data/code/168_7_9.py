from datetime import datetime

def group_timestamps_by_hour(timestamps):
    bucket = {}
    for ts in timestamps:
        dt = datetime.fromisoformat(ts)
        hour_key = dt.strftime('%Y-%m-%d %H')
        if hour_key not in bucket:
            bucket[hour_key] = []
        bucket[hour_key].append(dt)
    return bucket

if __name__ == '__main__':
    sample_timestamps = [
        '2023-10-01T14:30:00',
        '2023-10-01T15:45:00',
        '2023-10-01T16:00:00',
        '2023-10-02T14:15:00',
        '2023-10-02T14:45:00'
    ]
    result = group_timestamps_by_hour(sample_timestamps)
    print(result)