import re

def parse_time(time_str):
    hours = 0
    minutes = 0
    if 'hour' in time_str:
        hours_match = re.search('(\\d+)\\s*hours?', time_str)
        if hours_match:
            hours = int(hours_match.group(1))
    if 'minute' in time_str:
        minutes_match = re.search('(\\d+)\\s*minutes?', time_str)
        if minutes_match:
            minutes = int(minutes_match.group(1))
    return hours * 60 + minutes

def total_elapsed_time(time_list):
    total_minutes = sum((parse_time(time) for time in time_list))
    return total_minutes
if __name__ == '__main__':
    sample_times = ['2 hours 30 minutes', '1 hour 45 minutes', '30 minutes', '1 hour']
    result = total_elapsed_time(sample_times)
    print(result)