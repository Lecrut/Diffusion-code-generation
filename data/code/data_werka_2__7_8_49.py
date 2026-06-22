def convert_time(duration, unit):
    if unit == 'seconds':
        return {
            'minutes': duration / 60,
            'hours': duration / 3600,
            'days': duration / 86400
        }
    elif unit == 'minutes':
        return {
            'seconds': duration * 60,
            'hours': duration / 60,
            'days': duration / 1440
        }
    elif unit == 'hours':
        return {
            'seconds': duration * 3600,
            'minutes': duration * 60,
            'days': duration / 24
        }
    elif unit == 'days':
        return {
            'seconds': duration * 86400,
            'minutes': duration * 1440,
            'hours': duration * 24
        }
    else:
        raise ValueError("Unsupported unit. Please choose from 'seconds', 'minutes', 'hours', or 'days'.")

if __name__ == '__main__':
    try:
        sample_duration = 1
        sample_unit = 'hours'
        converted_times = convert_time(sample_duration, sample_unit)
        print(f"Converted times for {sample_duration} {sample_unit}:")
        for unit, value in converted_times.items():
            print(f"{unit}: {value}")
    except ValueError as e:
        print(e)