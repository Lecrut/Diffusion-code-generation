HOURS_TO_SECONDS = 3600
MINUTES_TO_SECONDS = 60

def parse_time_difference(diff):
    total_seconds = 0
    words = diff.split()
    i = 0
    while i < len(words):
        count_str = words[i]
        try:
            count = int(count_str)
        except ValueError:
            raise ValueError(f"Invalid numeric value: {count_str}")
        
        if i + 1 >= len(words):
            raise ValueError(f"Missing unit for value: {count_str}")
        
        unit = words[i + 1].lower()
        if 'hour' in unit:
            total_seconds += count * HOURS_TO_SECONDS
        elif 'minute' in unit:
            total_seconds += count * MINUTES_TO_SECONDS
        else:
            raise ValueError(f"Unsupported unit: {unit}")
        
        i += 2
    
    return total_seconds

def aggregate_time_differences(time_diffs):
    total_seconds = 0
    for diff in time_diffs:
        total_seconds += parse_time_difference(diff)
    return total_seconds

if __name__ == '__main__':
    sample_time_diffs = [
        "2 hours and 30 minutes",
        "1 hour 45 minutes",
        "30 minutes"
    ]
    print(aggregate_time_differences(sample_time_diffs))