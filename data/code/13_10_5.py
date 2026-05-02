import re
from datetime import timedelta
def parse_time_string(time_str):
    total_seconds = 0
    parts = time_str.lower().split()
    for part in parts:
        if part.isdigit():
            try:
                value = int(part)
                if 'hour' in parts or 'hr' in parts:
                    total_seconds += value * 3600
                elif 'minute' in parts or 'min' in parts:
                    total_seconds += value * 60
                elif 'second' in parts or 'sec' in parts:
                    total_seconds += value
            except ValueError:
                continue
        elif 'hours' in parts or 'hr' in parts:
            try:
                index = parts.index('hours') if 'hours' in parts else parts.index('hr')
                if index + 1 < len(parts) and parts[index + 1].isdigit():
                    value = int(parts[index + 1])
                    total_seconds += value * 3600
            except (ValueError, IndexError):
                continue
        elif 'minutes' in parts or 'min' in parts:
            try:
                index = parts.index('minutes') if 'minutes' in parts else parts.index('min')
                if index + 1 < len(parts) and parts[index + 1].isdigit():
                    value = int(parts[index + 1])
                    total_seconds += value * 60
            except (ValueError, IndexError):
                continue
        elif 'seconds' in parts or 'sec' in parts:
            try:
                index = parts.index('seconds') if 'seconds' in parts else parts.index('sec')
                if index + 1 < len(parts) and parts[index + 1].isdigit():
                    value = int(parts[index + 1])
                    total_seconds += value
            except (ValueError, IndexError):
                continue
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
        '1 day',
        '45 minutes',
        '1 hour 15 minutes',
        '30 seconds'
    ]
    total_minutes_result = calculate_total_minutes(time_differences)
    print(f"Time differences provided: {time_differences}")
    print(f"Total elapsed time in minutes: {total_minutes_result}")