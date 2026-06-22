def aggregate_time_differences(time_diffs):
    total_seconds = 0
    for time_diff in time_diffs:
        parts = time_diff.split()
        if len(parts) != 2:
            raise ValueError(f"Invalid time difference format: {time_diff}")
        
        value, unit = parts
        try:
            value = int(value)
        except ValueError:
            raise ValueError(f"Invalid numeric value in time difference: {value}")
        
        if unit == 'hours':
            total_seconds += value * 3600
        elif unit == 'minutes':
            total_seconds += value * 60
        else:
            raise ValueError(f"Unsupported unit in time difference: {unit}")
    
    return total_seconds

if __name__ == '__main__':
    sample_time_diffs = ["2 hours", "30 minutes", "1 hour", "45 minutes"]
    total_seconds = aggregate_time_differences(sample_time_diffs)
    print(total_seconds)