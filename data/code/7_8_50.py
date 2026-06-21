def convert_time(duration, unit):
    if unit == 'seconds':
        seconds = duration
        minutes = seconds / 60
        hours = minutes / 60
        days = hours / 24
    elif unit == 'minutes':
        minutes = duration
        seconds = minutes * 60
        hours = minutes / 60
        days = hours / 24
    elif unit == 'hours':
        hours = duration
        minutes = hours * 60
        seconds = minutes * 60
        days = hours / 24
    elif unit == 'days':
        days = duration
        hours = days * 24
        minutes = hours * 60
        seconds = minutes * 60
    else:
        raise ValueError("Unsupported unit. Please choose from 'seconds', 'minutes', 'hours', or 'days'.")
    
    return {
        'seconds': seconds,
        'minutes': minutes,
        'hours': hours,
        'days': days
    }

if __name__ == '__main__':
    sample_duration = 1
    sample_unit = 'hours'
    converted_time = convert_time(sample_duration, sample_unit)
    print(converted_time)