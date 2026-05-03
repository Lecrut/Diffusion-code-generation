import re
from datetime import timedelta
def parse_time_string(time_str):
    total_seconds = 0
    parts = time_str.lower().split()
    for part in parts:
        if 'hour' in part:
            try:
                hours = int(re.search(r'(\d+)\s*hour', part).group(1))
                total_seconds += hours * 3600
            except AttributeError:
                pass
        elif 'minute' in part:
            try:
                minutes = int(re.search(r'(\d+)\s*minute', part).group(1))
                total_seconds += minutes * 60
            except AttributeError:
                pass
    return total_seconds
def calculate_total_minutes(time_list):
    total_minutes = 0
    for time_str in time_list:
        total_seconds = parse_time_string(time_str)
        total_minutes += total_seconds / 60
    return total_minutes
if __name__ == '__main__':
    time_differences = [
        '2 hours 30 minutes',
        '1 day 5 hours',
        '45 minutes',
        '1 hour 15 minutes',
        '30 minutes'
    ]
    total_minutes = calculate_total_minutes(time_differences)
    print(f"Time differences provided: {time_differences}")
    print(f"Total elapsed time in minutes: {total_minutes}")