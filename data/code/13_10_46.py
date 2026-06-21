from datetime import timedelta

def parse_time_difference(time_str):
    if 'day' in time_str or 'days' in time_str:
        days, rest = time_str.split(' ', 1)
        hours, minutes, seconds = map(int, rest.split(':'))
        return timedelta(days=int(days), hours=hours, minutes=minutes, seconds=seconds)
    elif 'hour' in time_str or 'hours' in time_str:
        parts = time_str.split(':')
        if len(parts) == 3:
            hours, minutes, seconds = map(int, parts)
        else:
            hours = int(parts[0])
            minutes = int(parts[1]) if len(parts) > 1 else 0
            seconds = int(parts[2]) if len(parts) > 2 else 0
        return timedelta(hours=hours, minutes=minutes, seconds=seconds)
    elif 'minute' in time_str or 'minutes' in time_str:
        parts = time_str.split(':')
        if len(parts) == 2:
            minutes, seconds = map(int, parts)
        else:
            minutes = int(parts[0])
            seconds = int(parts[1]) if len(parts) > 1 else 0
        return timedelta(minutes=minutes, seconds=seconds)
    elif 'second' in time_str or 'seconds' in time_str:
        return timedelta(seconds=int(time_str))
    else:
        raise ValueError(f'Unsupported time format: {time_str}')

def scale_time_differences(time_diff_strings):
    standardized_timedeltas = []
    for time_str in time_diff_strings:
        try:
            td = parse_time_difference(time_str)
            standardized_timedeltas.append(td)
        except Exception as e:
            print(f"Error parsing '{time_str}': {e}")
    return standardized_timedeltas

if __name__ == '__main__':
    sample_values = [
        "2 days 5:30:15",
        "7 hours 45 minutes",
        "120 seconds",
        "30 minutes",
        "invalid format"
    ]
    result = scale_time_differences(sample_values)
    print(result)