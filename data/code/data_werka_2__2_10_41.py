def convert_volumes_to_milliliters(volumes):
    conversion_factors = {
        'liters': 1000,
        'gallons': 3785.41,
        'cubic_inches': 16.3871
    }
    
    converted_volumes = []
    for volume in volumes:
        value, unit = volume['value'], volume['unit'].lower()
        
        if value < 0:
            raise ValueError("Volume values cannot be negative.")
        
        if unit not in conversion_factors:
            raise ValueError(f"Unsupported unit: {unit}")
        
        converted_value = value * conversion_factors[unit]
        converted_volumes.append(converted_value)
    
    return converted_volumes

if __name__ == '__main__':
    sample_volumes = [
        {'value': 2, 'unit': 'liters'},
        {'value': 1, 'unit': 'gallons'},
        {'value': 1000, 'unit': 'cubic inches'}
    ]
    
    try:
        result = convert_volumes_to_milliliters(sample_volumes)
        print(result)
    except ValueError as e:
        print(e)