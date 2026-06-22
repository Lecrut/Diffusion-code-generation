def convert_volume(value, source_unit, target_unit='ml'):
    units_to_ml = {
        'ml': 1.0,
        'liter': 1000.0,
        'l': 1000.0,
        'gallon': 3785.41,
        'gal': 3785.41,
        'quart': 946.353,
        'qt': 946.353,
        'pint': 473.176,
        'pt': 473.176,
        'cup': 236.588,
        'fluid_ounce': 29.5735,
        'fl_oz': 29.5735,
        'tablespoon': 14.7868,
        'tbsp': 14.7868,
        'teaspoon': 4.92892,
        'tsp': 4.92892
    }
    
    try:
        source_key = source_unit.lower()
        target_key = target_unit.lower()
        
        if source_key not in units_to_ml:
            raise ValueError(f"Unsupported source unit: {source_unit}")
        if target_key not in units_to_ml:
            raise ValueError(f"Unsupported target unit: {target_unit}")
        
        if not isinstance(value, (int, float)):
            raise TypeError("Volume value must be a number")
            
        value_in_ml = value * units_to_ml[source_key]
        result = value_in_ml / units_to_ml[target_key]
        return result
    except ValueError as e:
        return str(e)
    except TypeError as e:
        return str(e)

if __name__ == '__main__':
    sample_value = 2.5
    sample_source = 'gallon'
    sample_target = 'liter'
    result = convert_volume(sample_value, sample_source, sample_target)
    print(f"{sample_value} {sample_source} equals {result} {sample_target}")
    
    sample_value2 = 1000
    sample_source2 = 'ml'
    sample_target2 = 'cup'
    result2 = convert_volume(sample_value2, sample_source2, sample_target2)
    print(f"{sample_value2} {sample_source2} equals {result2} {sample_target2}")
    
    invalid_unit = 'cup'
    invalid_source = 'xyz'
    result3 = convert_volume(10, invalid_source, invalid_unit)
    print(result3)