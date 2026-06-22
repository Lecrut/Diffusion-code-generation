def convert_volumes_to_ml(volumes):
    conversion_factors = {
        'liters': 1000.0,
        'gallons': 3785.41,
        'cubic_inches': 16.387064,
    }
    
    results = []
    for value, unit in volumes:
        if unit not in conversion_factors:
            raise ValueError(f"Unsupported unit: {unit}")
        
        if value < 0:
            return None
        
        results.append(value * conversion_factors[unit])
    
    return results

if __name__ == '__main__':
    measurements = [
        (1.0, 'liters'),
        (1.0, 'gallons'),
        (1.0, 'cubic_inches'),
        (0.0, 'liters'),
        (-5.0, 'liters'),
        (10.5, 'liters'),
    ]
    
    result = convert_volumes_to_ml(measurements)
    print(result)