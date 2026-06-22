def convert_time(value, source_unit, target_unit):
    conversion_factors = {
        'seconds_to_minutes': 1/60,
        'minutes_to_seconds': 60,
        'hours_to_minutes': 60,
        'minutes_to_hours': 1/60,
        'seconds_to_hours': 1/3600,
        'hours_to_seconds': 3600
    }
    
    if source_unit == target_unit:
        return value
    
    key = f"{source_unit}_to_{target_unit}"
    if key in conversion_factors:
        return value * conversion_factors[key]
    else:
        raise ValueError("Invalid unit conversion")

if __name__ == '__main__':
    sample_values = [
        (3600, 'seconds', 'hours'),
        (120, 'minutes', 'seconds'),
        (45, 'hours', 'minutes')
    ]
    
    for value, source_unit, target_unit in sample_values:
        result = convert_time(value, source_unit, target_unit)
        print(f"{value} {source_unit} is {result} {target_unit}")