def validate_duration(duration):
    if not isinstance(duration, (int, float)):
        raise ValueError("Duration must be a number.")
    if duration < 0:
        raise ValueError("Duration cannot be negative.")

def validate_unit(unit):
    supported_units = ['seconds', 'minutes', 'hours', 'days']
    if unit not in supported_units:
        raise ValueError(f"Unsupported unit: {unit}")

def convert_time(duration, unit):
    validate_duration(duration)
    validate_unit(unit)
    
    UNIT_CONVERSIONS = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400
    }
    
    total_seconds = duration * UNIT_CONVERSIONS[unit]
    return {
        'seconds': total_seconds,
        'minutes': total_seconds / UNIT_CONVERSIONS['minutes'],
        'hours': total_seconds / UNIT_CONVERSIONS['hours'],
        'days': total_seconds / UNIT_CONVERSIONS['days']
    }

if __name__ == '__main__':
    sample_duration = 1
    sample_unit = 'hours'
    converted_time = convert_time(sample_duration, sample_unit)
    print(converted_time)