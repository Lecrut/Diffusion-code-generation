import math

def convert_distance(distance, target_unit, current_unit='meters'):
    if distance < 0:
        raise ValueError("Distance cannot be negative")
    
    conversion_factors = {
        'meters': 1.0,
        'kilometers': 1000.0,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'miles': 1609.344,
        'feet': 0.3048,
        'inches': 0.0254,
        'yards': 0.9144
    }
    
    if current_unit not in conversion_factors:
        raise ValueError(f"Invalid current unit: {current_unit}")
    if target_unit not in conversion_factors:
        raise ValueError(f"Invalid target unit: {target_unit}")
    
    base_value = distance * conversion_factors[current_unit]
    result = base_value / conversion_factors[target_unit]
    
    return result

if __name__ == '__main__':
    sample_distance = 1500.0
    source = 'meters'
    target = 'feet'
    converted_value = convert_distance(sample_distance, target, source)
    print(converted_value)
    
    try:
        invalid_conversion = convert_distance(100.0, 'invalid_unit', 'meters')
        print(invalid_conversion)
    except ValueError as e:
        print(f"Error caught: {e}")
    
    print(convert_distance(1.0, 'kilometers', 'meters'))
    print(convert_distance(1.0, 'meters', 'kilometers'))