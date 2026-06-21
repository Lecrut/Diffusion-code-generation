def convert_volume(value, source_unit, target_unit='milliliters'):
    conversion_rates = {
        'milliliters': 1.0,
        'liters': 1000.0,
        'cubic_meters': 1000000.0,
        'teaspoons': 4.92892,
        'tablespoons': 14.7868,
        'fluid_ounces': 29.5735,
        'cups': 236.588,
        'pints': 473.176,
        'quarts': 946.353,
        'gallons': 3785.41,
        'imperial_teaspoons': 5.91939,
        'imperial_tablespoons': 17.7582,
        'imperial_fluid_ounces': 28.4131,
        'imperial_cups': 284.131,
        'imperial_pints': 568.261,
        'imperial_quarts': 1136.52,
        'imperial_gallons': 4546.09
    }
    
    if source_unit not in conversion_rates:
        raise ValueError(f"Unsupported source unit: {source_unit}")
    
    if target_unit not in conversion_rates:
        raise ValueError(f"Unsupported target unit: {target_unit}")
    
    try:
        numeric_value = float(value)
    except (ValueError, TypeError):
        raise ValueError("Volume value must be a number")
    
    value_in_ml = numeric_value * conversion_rates[source_unit]
    result = value_in_ml / conversion_rates[target_unit]
    return result

if __name__ == '__main__':
    sample_value = 2.5
    sample_source = 'gallons'
    sample_target = 'liters'
    print(convert_volume(sample_value, sample_source, sample_target))
    print(convert_volume(100, 'milliliters', 'teaspoons'))
    print(convert_volume(1, 'imperial_gallons', 'liters'))