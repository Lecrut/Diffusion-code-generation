def convert_time(value, source_unit, target_unit):
    conversion_factors = {
        'seconds': {'minutes': 1/60, 'hours': 1/3600},
        'minutes': {'seconds': 60, 'hours': 1/60},
        'hours': {'seconds': 3600, 'minutes': 60}
    }
    
    if source_unit not in conversion_factors or target_unit not in conversion_factors:
        raise ValueError("Invalid unit. Use 'seconds', 'minutes', or 'hours'.")
    
    if source_unit == target_unit:
        return value
    
    conversion_factor = conversion_factors[source_unit][target_unit]
    converted_value = value * conversion_factor
    return converted_value

if __name__ == '__main__':
    sample_values = [
        (3600, 'seconds', 'hours'),
        (120, 'minutes', 'seconds'),
        (5, 'hours', 'minutes')
    ]
    
    for value, source_unit, target_unit in sample_values:
        result = convert_time(value, source_unit, target_unit)
        print(f"{value} {source_unit} is equal to {result} {target_unit}")