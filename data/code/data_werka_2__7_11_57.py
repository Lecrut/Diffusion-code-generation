def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

def seconds_to_human_readable(total_seconds):
    units = {'day': 24 * 3600, 'hour': 3600, 'minute': 60}
    result = []
    for unit_name, unit_seconds in units.items():
        if total_seconds >= unit_seconds:
            quantity = total_seconds // unit_seconds
            result.append(f"{quantity} {unit_name}{'' if quantity == 1 else 's'}")
            total_seconds %= unit_seconds
    return ', '.join(result) or "0 seconds"

def convert_time(time_str):
    total_seconds = time_to_seconds(time_str)
    human_readable = seconds_to_human_readable(total_seconds)
    return human_readable

if __name__ == '__main__':
    sample_time = '36:75:90'
    result = convert_time(sample_time)
    print(result)