import re

def parse_time_difference(time_str):
    hour_pattern = '(\\d+)\\s*hours?'
    minute_pattern = '(\\d+)\\s*minutes?'
    hours_match = re.search(hour_pattern, time_str)
    minutes_match = re.search(minute_pattern, time_str)
    hours = int(hours_match.group(1)) if hours_match else 0
    minutes = int(minutes_match.group(1)) if minutes_match else 0
    total_minutes = hours * 60 + minutes
    return total_minutes

def calculate_total_elapsed_time(time_differences):
    total_minutes = sum((parse_time_difference(td) for td in time_differences))
    return total_minutes
if __name__ == '__main__':
    sample_times = ['2 hours 30 minutes', '1 hour 45 minutes', '30 minutes', '4 hours']
    total_time = calculate_total_elapsed_time(sample_times)
    print(total_time)