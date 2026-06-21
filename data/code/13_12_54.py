import re

def aggregate_durations(time_diffs):
    total_seconds = 0
    time_pattern = re.compile(r'(\d+)\s*(hours?|minutes?)')
    
    for diff in time_diffs:
        matches = time_pattern.findall(diff)
        for count, unit in matches:
            if 'hour' in unit:
                total_seconds += int(count) * 3600
            elif 'minute' in unit:
                total_seconds += int(count) * 60
    
    return total_seconds

if __name__ == '__main__':
    sample_durations = [
        "2 hours and 30 minutes",
        "1 hour 45 minutes",
        "30 minutes"
    ]
    
    print(aggregate_durations(sample_durations))