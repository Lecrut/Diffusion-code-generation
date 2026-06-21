import re

def aggregate_time_differences(time_diffs):
    total_seconds = 0
    time_pattern = re.compile(r'(\d+)\s*(hours?|minutes?)')
    
    for diff in time_diffs:
        matches = time_pattern.findall(diff)
        for count, unit in matches:
            if unit.startswith('hour'):
                total_seconds += int(count) * 3600
            elif unit.startswith('min'):
                total_seconds += int(count) * 60
    
    return total_seconds

if __name__ == '__main__':
    sample_time_diffs = [
        "2 hours and 30 minutes",
        "1 hour 45 minutes",
        "30 minutes"
    ]
    
    total_seconds = aggregate_time_differences(sample_time_diffs)
    print(total_seconds)