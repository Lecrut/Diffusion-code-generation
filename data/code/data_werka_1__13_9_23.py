import re

def parse_time_difference(time_str):
    total_minutes = 0
    time_units = {'hour': 60, 'minute': 1, 'second': 1 / 60}
    pattern = '(\\d+)\\s*(hours?|minutes?|seconds?)'
    matches = re.findall(pattern, time_str)
    for number, unit in matches:
        number = int(number)
        if unit.endswith('s'):
            unit = unit.rstrip('s')
        total_minutes += number * time_units[unit]
    return round(total_minutes)

def calculate_total_time(time_differences):
    total_minutes = 0
    for time_str in time_differences:
        total_minutes += parse_time_difference(time_str)
    return total_minutes
if __name__ == '__main__':
    sample_times = ['2 hours 30 minutes', '1 hour 45 minutes', '30 minutes', '1 hour']
    total_time = calculate_total_time(sample_times)
    print(total_time)