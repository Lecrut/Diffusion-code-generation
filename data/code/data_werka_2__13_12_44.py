def aggregate_durations(time_diffs):
    total_seconds = 0
    for time_str in time_diffs:
        parts = time_str.split()
        if len(parts) != 2:
            raise ValueError(f"Invalid time difference format: {time_str}")
        
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
            raise ValueError(f"Unsupported unit: {unit}")
    
    return total_seconds

if __name__ == '__main__':
    sample_time_diffs = ["2 hours", "45 minutes", "1 hour"]
    total_duration = aggregate_durations(sample_time_diffs)
    print(total_duration)