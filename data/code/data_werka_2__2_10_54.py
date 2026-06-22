def convert_volumes_to_milliliters(volumes):
    LITERS_TO_MILLILITERS = 1000
    GALLONS_TO_MILLILITERS = 3785.41
    CUBIC_INCHES_TO_MILLILITERS = 16.3871
    
    conversion_factors = {
        'liters': LITERS_TO_MILLILITERS,
        'gallons': GALLONS_TO_MILLILITERS,
        'cubic_inches': CUBIC_INCHES_TO_MILLILITERS
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
        {'value': 2.5, 'unit': 'liters'},
        {'value': 10, 'unit': 'gallons'},
        {'value': 100, 'unit': 'cubic inches'}
    ]
    
    converted = convert_volumes_to_milliliters(sample_volumes)
    print(converted)