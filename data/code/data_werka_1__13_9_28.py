import re

def parse_time_difference(time_str):
    pattern = '(\\d+)\\s+hours\\s+(\\d+)\\s+minutes'
    match = re.match(pattern, time_str)
    if match:
        hours = int(match.group(1))
        minutes = int(match.group(2))
        return hours * 60 + minutes
    else:
        raise ValueError('Invalid time format')

def calculate_total_time(time_differences):
    total_minutes = 0
    for time_str in time_differences:
        total_minutes += parse_time_difference(time_str)
    return total_minutes
if __name__ == '__main__':
    sample_times = ['2 hours 30 minutes', '1 hour 45 minutes', '3 hours 15 minutes']
    total_time = calculate_total_time(sample_times)
    print(total_time)