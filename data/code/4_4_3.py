def convert_distance(distance: float, target_unit: str, base_unit: str = 'meters', conversion_factors: dict = None) -> float:
    if conversion_factors is None:
        conversion_factors = {
            'meters': 1.0,
            'kilometers': 1000.0,
            'centimeters': 0.01,
            'millimeters': 0.001,
            'miles': 1609.344,
            'yards': 0.9144,
            'feet': 0.3048,
            'inches': 0.0254
        }
    
    if target_unit not in conversion_factors:
        raise ValueError(f"Unsupported target unit: {target_unit}")
    
    if base_unit not in conversion_factors:
        raise ValueError(f"Unsupported base unit: {base_unit}")
    
    base_factor = conversion_factors[base_unit]
    target_factor = conversion_factors[target_unit]
    
    if target_factor == 0:
        raise ZeroDivisionError("Division by zero encountered: target unit has a conversion factor of zero")
    
    converted_distance = (distance * base_factor) / target_factor
    return converted_distance

if __name__ == '__main__':
    result_miles = convert_distance(1000.0, 'miles', 'meters')
    print(result_miles)
    
    result_inches = convert_distance(1.0, 'inches', 'feet')
    print(result_inches)
    
    result_kilometers = convert_distance(5280.0, 'kilometers', 'feet')
    print(result_kilometers)