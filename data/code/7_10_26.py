def convert_time(duration, unit):
    conversion_factors = {'seconds': 1, 'minutes': 60, 'hours': 3600, 'days': 86400}
    if unit not in conversion_factors:
        raise ValueError("Invalid unit. Please choose from 'seconds', 'minutes', 'hours', or 'days'.")
    total_seconds = duration * conversion_factors[unit]
    converted_units = {'seconds': total_seconds, 'minutes': total_seconds / 60, 'hours': total_seconds / 3600, 'days': total_seconds / 86400}
    return converted_units
if __name__ == '__main__':
    duration = 12
    unit = 'hours'
    result = convert_time(duration, unit)
    print(result)