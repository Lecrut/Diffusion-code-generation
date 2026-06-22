from datetime import timedelta

def parse_time_difference(time_str):
    if 'day' in time_str:
        days, rest = time_str.split(' day')
        hours, minutes, seconds = map(int, rest.split(':'))
        return timedelta(days=int(days), hours=hours, minutes=minutes, seconds=seconds)
    elif 'hour' in time_str:
        parts = time_str.split(':')
        if len(parts) == 3:
            hours, minutes, seconds = map(int, parts)
        else:
            hours = int(parts[0])
            minutes = int(parts[1]) if len(parts) > 1 else 0
            seconds = int(parts[2]) if len(parts) > 2 else 0
        return timedelta(hours=hours, minutes=minutes, seconds=seconds)
    else:
        raise ValueError(f'Unsupported time format: {time_str}')

def scale_time_differences(time_diff_strings):
    scaled_timedeltas = []
    for time_str in time_diff_strings:
        try:
            td = parse_time_difference(time_str)
            scaled_timedeltas.append(td)
        except Exception as e:
            print(f"Error parsing '{time_str}': {e}")
    return scaled_timedeltas

if __name__ == '__main__':
    sample_time_differences = [
        "1 day 12:30:45",
        "5 hours 30 minutes",
        "2 days 7 hours 45 seconds",
        "unsupported format"
    ]
    result = scale_time_differences(sample_time_differences)
    print(result)