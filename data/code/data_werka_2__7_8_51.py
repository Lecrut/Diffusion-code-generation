def convert_time(duration, unit):
    if unit == 'seconds':
        return {
            'seconds': duration,
            'minutes': duration / 60,
            'hours': duration / 3600,
            'days': duration / 86400
        }
    elif unit == 'minutes':
        return {
            'seconds': duration * 60,
            'minutes': duration,
            'hours': duration / 60,
            'days': duration / 1440
        }
    elif unit == 'hours':
        return {
            'seconds': duration * 3600,
            'minutes': duration * 60,
            'hours': duration,
            'days': duration / 24
        }
    elif unit == 'days':
        return {
            'seconds': duration * 86400,
            'minutes': duration * 1440,
            'hours': duration * 24,
            'days': duration
        }
    else:
        raise ValueError("Unsupported unit. Please choose from 'seconds', 'minutes', 'hours', or 'days'.")

if __name__ == '__main__':
    sample_duration = 1
    sample_unit = 'hours'
    converted_time = convert_time(sample_duration, sample_unit)
    print(converted_time)