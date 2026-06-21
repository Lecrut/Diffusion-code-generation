def validate_time_format(time_str):
    try:
        hours, minutes, seconds = map(int, time_str.split(':'))
        if not (0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59):
            raise ValueError('Invalid time format. Hours must be between 0-23, minutes and seconds between 0-59.')
    except ValueError as e:
        raise ValueError(f'Invalid input: {e}')

def convert_time_to_seconds(time_str):
    validate_time_format(time_str)
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

def convert_seconds_to_human_readable(total_seconds):
    if total_seconds < 0:
        raise ValueError('Total seconds cannot be negative.')
    
    days = total_seconds // (24 * 3600)
    remaining_seconds = total_seconds % (24 * 3600)
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    
    return f"{days} days, {hours} hours, {minutes} minutes"

def convert_time(time_str):
    total_seconds = convert_time_to_seconds(time_str)
    human_readable = convert_seconds_to_human_readable(total_seconds)
    return human_readable

if __name__ == '__main__':
    sample_time = '12:34:56'
    result = convert_time(sample_time)
    print(result)