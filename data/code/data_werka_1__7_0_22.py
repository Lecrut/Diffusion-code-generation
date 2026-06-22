def convert_time(value, source_unit, target_unit):
    conversion_factors = {
        'seconds_to_minutes': 1/60,
        'minutes_to_seconds': 60,
        'minutes_to_hours': 1/60,
        'hours_to_minutes': 60,
        'seconds_to_hours': 1/3600,
        'hours_to_seconds': 3600
    }
    
    if source_unit == target_unit:
        return value
    
    conversion_key = f"{source_unit}_to_{target_unit}"
    if conversion_key in conversion_factors:
        return value * conversion_factors[conversion_key]
    else:
        raise ValueError("Unsupported conversion")

if __name__ == '__main__':
    sample_values = [
        (3600, 'seconds', 'hours'),
        (60, 'minutes', 'seconds'),
        (2, 'hours', 'minutes')
    ]
    
    for value, source_unit, target_unit in sample_values:
        result = convert_time(value, source_unit, target_unit)
        print(f"{value} {source_unit} is equal to {result} {target_unit}")