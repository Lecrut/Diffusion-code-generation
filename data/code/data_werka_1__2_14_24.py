def convert_volumes_to_milliliters(volumes):
    conversion_factors = {
        'liters': 1000,
        'gallons': 3785.41,
        'cubic_inches': 16.3871
    }
    
    converted_volumes = []
    for volume in volumes:
        value, unit = volume
        if value <= 0:
            converted_volumes.append(0)
        else:
            try:
                conversion_factor = conversion_factors[unit]
                converted_volume = value * conversion_factor
                converted_volumes.append(converted_volume)
            except KeyError:
                converted_volumes.append(None)
    
    return converted_volumes

if __name__ == '__main__':
    sample_volumes = [
        (2, 'liters'),
        (1, 'gallons'),
        (1000, 'cubic_inches'),
        (0, 'liters'),
        (-5, 'gallons'),
        (3.5, 'unknown_unit')
    ]
    
    converted = convert_volumes_to_milliliters(sample_volumes)
    print(converted)