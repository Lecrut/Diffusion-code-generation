import re
from datetime import timedelta
def parse_time_string(time_str):
    total_seconds = 0
    parts = time_str.lower().split()
    if not parts:
        return 0
    for part in parts:
        if part.isdigit():
            try:
                value = int(part)
                if 'hour' in parts or 'h' in parts:
                    total_seconds += value * 3600
                elif 'minute' in parts or 'm' in parts:
                    total_seconds += value * 60
                elif 'second' in parts or 's' in parts:
                    total_seconds += value
            except ValueError:
                continue
        elif 'hours' in parts or 'h' in parts:
            try:
                index = parts.index('hours') if 'hours' in parts else parts.index('h')
                if index + 1 < len(parts) and parts[index + 1].isdigit():
                    total_seconds += int(parts[index + 1]) * 3600
            except (ValueError, IndexError):
                pass
        elif 'minutes' in parts or 'm' in parts:
            try:
                index = parts.index('minutes') if 'minutes' in parts else parts.index('m')
                if index + 1 < len(parts) and parts[index + 1].isdigit():
                    total_seconds += int(parts[index + 1]) * 60
            except (ValueError, IndexError):
                pass
        elif 'seconds' in parts or 's' in parts:
            try:
                index = parts.index('seconds') if 'seconds' in parts else parts.index('s')
                if index + 1 < len(parts) and parts[index + 1].isdigit():
                    total_seconds += int(parts[index + 1])
            except (ValueError, IndexError):
                pass
    return total_seconds
def calculate_total_minutes(time_list):
    total_seconds = 0
    for time_str in time_list:
        total_seconds += parse_time_string(time_str)
    total_minutes = total_seconds // 60
    return total_minutes
if __name__ == '__main__':
    time_differences = [
        '2 hours 30 minutes',
        '1 day',
        '45 minutes',
        '1 hour 15 minutes',
        '30 seconds'
    ]
    total_minutes = calculate_total_minutes(time_differences)
    print(f"Time differences provided: {time_differences}")
    print(f"Total elapsed time in minutes: {total_minutes}")