def convert_length(value: float, unit_from: str) -> dict:
    conversions = {
        'm': value,
        'km': value * 1000,
        'cm': value * 100,
        'mm': value * 1000,
        'ft': value * 3.28084,
        'in': value * 39.3701,
        'yd': value * 1.09361,
        'mi': value * 0.000621371,
    }
    
    if unit_from not in conversions:
        raise ValueError(f"Unsupported unit: {unit_from}")
        
    meters = conversions[unit_from]
    
    results = {
        'meters': meters,
        'kilometers': meters / 1000,
        'centimeters': meters * 100,
        'millimeters': meters * 1000,
        'feet': meters * 3.28084,
        'inches': meters * 39.3701,
        'yards': meters * 1.09361,
        'miles': meters * 0.000621371,
    }
    
    return results

if __name__ == '__main__':
    sample_value = 5.0
    sample_unit = 'km'
    
    result = convert_length(sample_value, sample_unit)
    
    for unit, converted_value in result.items():
        print(f"{sample_value} {sample_unit} is {converted_value:.4f} {unit}")