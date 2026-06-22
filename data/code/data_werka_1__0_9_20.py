def convert_measurements(measurements, unit):
    conversions = {
        'kilometers': {'meters': 1000, 'feet': 3280.84},
        'meters': {'meters': 1, 'feet': 3.28084},
        'feet': {'meters': 0.3048, 'feet': 1},
        'centimeters': {'meters': 0.01, 'feet': 0.0328084}
    }
    
    if unit not in conversions:
        raise ValueError(f"Unsupported unit: {unit}")
        
    results = []
    for val in measurements:
        meters = val * conversions[unit]['meters']
        feet = val * conversions[unit]['feet']
        results.append((val, meters, feet))
        
    return results

if __name__ == '__main__':
    sample_data = [1.0, 5.5, 100]
    unit = 'kilometers'
    
    converted = convert_measurements(sample_data, unit)
    
    for original, meters, feet in converted:
        print(f"{original} {unit} = {meters} meters = {feet} feet")