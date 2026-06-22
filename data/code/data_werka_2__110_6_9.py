from datetime import datetime, timezone

def sort_unix_timestamps(timestamps):
    if not isinstance(timestamps, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    if len(timestamps) == 0:
        return []
    
    validated_timestamps = []
    for ts in timestamps:
        if not isinstance(ts, (int, float)):
            raise ValueError("All elements must be numeric")
        if isinstance(ts, float) and ts != int(ts):
            raise ValueError("Float timestamps must be whole numbers")
        validated_timestamps.append(int(ts))
    
    if len(set(validated_timestamps)) != len(validated_timestamps):
        raise ValueError("Timestamps must be unique")
    
    def to_datetime(ts):
        return datetime.fromtimestamp(ts, tz=timezone.utc)
    
    sorted_timestamps = sorted(validated_timestamps, key=to_datetime)
    return sorted_timestamps

if __name__ == '__main__':
    sample_timestamps = [1700000000, 1600000000, 1800000000, 1500000000, 1650000000]
    result = sort_unix_timestamps(sample_timestamps)
    print(result)