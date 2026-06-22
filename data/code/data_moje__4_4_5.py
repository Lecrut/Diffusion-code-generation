def convert_distance(distance, target_unit):
    units = {
        'meter': 1.0,
        'kilometer': 0.001,
        'mile': 0.000621371192237334,
        'foot': 3.28083989501312,
        'yard': 1.09361329833771,
        'inch': 39.3700787401575,
        'centimeter': 100.0,
        'millimeter': 1000.0
    }
    
    if target_unit.lower() not in units:
        raise ValueError(f"Unsupported target unit: {target_unit}")
    
    if distance < 0:
        raise ValueError("Distance cannot be negative")
    
    base_unit_value = distance * units[target_unit.lower()]
    return base_unit_value

if __name__ == '__main__':
    sample_distance = 100
    sample_target_unit = 'kilometer'
    result = convert_distance(sample_distance, sample_target_unit)
    print(result)