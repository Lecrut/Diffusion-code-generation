def convert_time(value, unit):
    conversions = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400
    }
    if unit not in conversions:
        raise ValueError(f"Unsupported unit: {unit}")
    if value < 0:
        raise ValueError("Value must be non-negative")
    total_seconds = value * conversions[unit]
    days = total_seconds / 86400
    hours = (total_seconds % 86400) / 3600
    minutes = (total_seconds % 3600) / 60
    seconds = total_seconds % 60
    return {
        'seconds': total_seconds,
        'minutes': total_seconds / 60,
        'hours': total_seconds / 3600,
        'days': total_seconds / 86400
    }

if __name__ == '__main__':
    result = convert_time(90, 'minutes')
    print(result)