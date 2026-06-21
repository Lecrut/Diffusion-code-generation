def convert_time(duration, unit):
    units = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400
    }
    
    if unit not in units:
        raise ValueError(f"Unsupported unit: {unit}")
    
    seconds = duration * units[unit]
    
    return {
        'seconds': seconds,
        'minutes': seconds / units['minutes'],
        'hours': seconds / units['hours'],
        'days': seconds / units['days']
    }

if __name__ == '__main__':
    try:
        sample_duration = 1
        sample_unit = 'hours'
        converted_time = convert_time(sample_duration, sample_unit)
        print(converted_time)
    except ValueError as e:
        print(e)