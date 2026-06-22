import re

def aggregate_time_differences(time_diffs):
    total_seconds = 0
    for time_str in time_diffs:
        hours_match = re.search(r'(\d+)h', time_str)
        minutes_match = re.search(r'(\d+)m', time_str)
        
        if hours_match:
            total_seconds += int(hours_match.group(1)) * 3600
        if minutes_match:
            total_seconds += int(minutes_match.group(1)) * 60
    
    return total_seconds

if __name__ == '__main__':
    sample_time_diffs = ["2h", "30m", "1h45m", "5m"]
    print(aggregate_time_differences(sample_time_diffs))