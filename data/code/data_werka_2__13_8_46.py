import re

def parse_time_difference(time_str):
    total_minutes = 0
    hour_pattern = '(\\d+)\\s*hours?'
    minute_pattern = '(\\d+)\\s*minutes?'
    hours_match = re.search(hour_pattern, time_str)
    minutes_match = re.search(minute_pattern, time_str)
    if hours_match:
        total_minutes += int(hours_match.group(1)) * 60
    if minutes_match:
        total_minutes += int(minutes_match.group(1))
    return total_minutes

def calculate_total_time(time_differences):
    total_minutes = 0
    for time_str in time_differences:
        total_minutes += parse_time_difference(time_str)
    return total_minutes
if __name__ == '__main__':
    sample_times = ['2 hours 30 minutes', '1 hour 45 minutes', '3 hours', '45 minutes']
    total_time = calculate_total_time(sample_times)
    print(total_time)