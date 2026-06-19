import re

def parse_time_difference(time_str):
    hours = 0
    minutes = 0
    hour_pattern = '(\\d+)\\s*hours?'
    minute_pattern = '(\\d+)\\s*minutes?'
    match = re.search(hour_pattern, time_str)
    if match:
        hours = int(match.group(1))
    match = re.search(minute_pattern, time_str)
    if match:
        minutes = int(match.group(1))
    total_minutes = hours * 60 + minutes
    return total_minutes

def calculate_total_time(time_differences):
    total_minutes = 0
    for time_diff in time_differences:
        total_minutes += parse_time_difference(time_diff)
    return total_minutes
if __name__ == '__main__':
    sample_times = ['2 hours 30 minutes', '1 hour', '45 minutes', '3 hours 15 minutes']
    total_time = calculate_total_time(sample_times)
    print(total_time)