def convert_duration(value, from_unit):
    units_to_seconds = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400
    }

    if from_unit not in units_to_seconds:
        raise ValueError(f"Invalid unit: {from_unit}")

    if value < 0:
        raise ValueError("Value must be non-negative")

    total_seconds = value * units_to_seconds[from_unit]

    converted = {
        'seconds': total_seconds,
        'minutes': total_seconds / 60,
        'hours': total_seconds / 3600,
        'days': total_seconds / 86400
    }

    return converted

if __name__ == '__main__':
    result = convert_duration(3661, 'seconds')
    print(result)