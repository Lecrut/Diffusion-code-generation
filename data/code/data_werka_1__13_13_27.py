import re

def aggregate_durations(time_diffs):
    total_seconds = 0
    time_pattern = re.compile(r'(\d+)\s*(hours?|minutes?)')
    
    for diff in time_diffs:
        matches = time_pattern.findall(diff)
        for count, unit in matches:
            count = int(count)
            if 'hour' in unit:
                total_seconds += count * 3600
            elif 'minute' in unit:
                total_seconds += count * 60
    
    return total_seconds

if __name__ == '__main__':
    sample_times = ["2 hours", "45 minutes", "1 hour 30 minutes", "30 mins"]
    print(aggregate_durations(sample_times))