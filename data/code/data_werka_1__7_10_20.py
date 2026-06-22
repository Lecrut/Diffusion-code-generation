def convert_time(duration, unit):
    conversions = {'seconds': 1, 'minutes': 60, 'hours': 3600, 'days': 86400}
    if unit not in conversions:
        raise ValueError(f'Invalid unit: {unit}. Supported units are: {list(conversions.keys())}')
    total_seconds = duration * conversions[unit]
    converted_units = {'seconds': total_seconds, 'minutes': total_seconds / 60, 'hours': total_seconds / 3600, 'days': total_seconds / 86400}
    return converted_units
if __name__ == '__main__':
    duration = 120
    unit = 'minutes'
    try:
        result = convert_time(duration, unit)
        print(result)
    except ValueError as e:
        print(e)