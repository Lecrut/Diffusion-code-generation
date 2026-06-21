from datetime import datetime

def group_timestamps_by_hour(timestamps):
    if not all((isinstance(ts, int) for ts in timestamps)):
        raise ValueError('All elements in the list must be integers representing Unix timestamps.')
    grouped = {}
    for ts in timestamps:
        dt = datetime.fromtimestamp(ts)
        hour_key = dt.strftime('%Y-%m-%d %H')
        if hour_key not in grouped:
            grouped[hour_key] = []
        grouped[hour_key].append(dt)
    return grouped
if __name__ == '__main__':
    sample_timestamps = [1672531200, 1672534800, 1672538400, 1672542000, 1672545600]
    print(group_timestamps_by_hour(sample_timestamps))