import re
def aggregate_time_differences(time_strings):
    total_seconds = 0
    for time_str in time_strings:
        total_seconds += parse_time_string(time_str)
    return total_seconds
def parse_time_string(time_str):
    total_seconds = 0
    if not time_str:
        return 0
    parts = time_str.split()
    for part in parts:
        if re.match(r'(\d+)\s*h', part):
            hours = int(re.search(r'(\d+)', part).group(1))
            total_seconds += hours * 3600
        elif re.match(r'(\d+)\s*m', part):
            minutes = int(re.search(r'(\d+)', part).group(1))
            total_seconds += minutes * 60
    return total_seconds
if __name__ == '__main__':
    sample_times = [
        "1 hour 30 minutes",
        "2 hours",
        "45 minutes",
        "1 day 5 hours"
    ]
    total_duration = aggregate_time_differences(sample_times)
    print(total_duration)