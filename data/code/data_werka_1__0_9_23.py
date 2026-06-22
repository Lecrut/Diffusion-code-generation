def convert_measurements(measurements, unit):
    conversions = {
        'km': {'m': 1000, 'ft': 3280.84},
        'm': {'m': 1, 'ft': 3.28084},
        'ft': {'m': 0.3048, 'ft': 1}
    }
    
    if unit not in conversions:
        raise ValueError(f"Unsupported unit: {unit}")
        
    factors = conversions[unit]
    results = []
    
    for val in measurements:
        meters = val * factors['m']
        feet = val * factors['ft']
        results.append((val, meters, feet))
        
    return results

if __name__ == '__main__':
    sample_data = [1.5, 2.0, 0.5]
    unit_type = 'km'
    
    converted_values = convert_measurements(sample_data, unit_type)
    
    for original, meters, feet in converted_values:
        print(f"{original} {unit_type} is {meters:.2f} meters and {feet:.2f} feet")