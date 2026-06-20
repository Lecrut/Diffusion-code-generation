def convert_volume(value, from_unit, to_unit):
    conversion_factors_to_liters = {
        'liter': 1.0,
        'liter': 1.0,
        'liters': 1.0,
        'milliliter': 0.001,
        'milliliters': 0.001,
        'milliliter': 0.001,
        'milliliters': 0.001,
        'cubic_meter': 1000.0,
        'cubic_meters': 1000.0,
        'cubic_meter': 1000.0,
        'cubic_meters': 1000.0,
        'gallon': 3.78541,
        'gallons': 3.78541,
        'cubic_inch': 0.016387064,
        'cubic_inches': 0.016387064
    }
    
    standard_to_liters = {
        'liter': 1.0,
        'milliliter': 0.001,
        'cubic_meter': 1000.0,
        'gallon': 3.78541,
        'cubic_inch': 0.016387064
    }
    
    standard_from_liters = {
        'liter': 1.0,
        'milliliter': 0.001,
        'cubic_meter': 1000.0,
        'gallon': 3.78541,
        'cubic_inch': 0.016387064
    }
    
    value_liters = value * standard_to_liters[from_unit]
    result_liters = value_liters
    
    if to_unit == 'liter':
        result = result_liters
    elif to_unit == 'milliliter':
        result = result_liters / standard_from_liters['milliliter']
    elif to_unit == 'cubic_meter':
        result = result_liters / standard_from_liters['cubic_meter']
    elif to_unit == 'gallon':
        result = result_liters / standard_from_liters['gallon']
    elif to_unit == 'cubic_inch':
        result = result_liters / standard_from_liters['cubic_inch']
    else:
        raise ValueError(f"Unsupported unit: {to_unit}")
        
    return result

def main():
    val = 5.0
    src = 'liter'
    dst = 'milliliter'
    res = convert_volume(val, src, dst)
    print(res)
    
    val2 = 10.0
    src2 = 'gallon'
    dst2 = 'liter'
    res2 = convert_volume(val2, src2, dst2)
    print(res2)

if __name__ == '__main__':
    main()