def convert_time(duration, unit):
    conversion_factors = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400
    }
    
    if unit not in conversion_factors:
        raise ValueError("Invalid time unit. Supported units are: seconds, minutes, hours, days.")
    
    seconds = duration * conversion_factors[unit]
    
    return {
        'seconds': seconds,
        'minutes': seconds / conversion_factors['minutes'],
        'hours': seconds / conversion_factors['hours'],
        'days': seconds / conversion_factors['days']
    }

if __name__ == '__main__':
    try:
        sample_duration = 1
        sample_unit = 'hours'
        converted_time = convert_time(sample_duration, sample_unit)
        print(converted_time)
    except Exception as e:
        print(e)