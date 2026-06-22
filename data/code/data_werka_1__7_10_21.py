def convert_time(duration, unit):
    units = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400
    }
    
    if unit not in units:
        raise ValueError("Invalid unit. Please choose from 'seconds', 'minutes', 'hours', or 'days'.")
    
    seconds = duration * units[unit]
    
    return {
        'seconds': seconds,
        'minutes': seconds / 60,
        'hours': seconds / 3600,
        'days': seconds / 86400
    }

if __name__ == '__main__':
    try:
        sample_duration = 1
        sample_unit = 'hours'
        converted_time = convert_time(sample_duration, sample_unit)
        print(converted_time)
    except Exception as e:
        print(e)