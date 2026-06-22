def convert_volume(value, source_unit, target_unit='liters'):
    conversion_rates = {
        'liters': 1.0,
        'milliliters': 0.001,
        'gallons_us': 3.78541,
        'gallons_uk': 4.54609,
        'quarts_us': 0.946353,
        'quarts_uk': 1.13652,
        'pints_us': 0.473176,
        'pints_uk': 0.568261,
        'cups_us': 0.236588,
        'fluid_ounces_us': 0.0295735,
        'fluid_ounces_uk': 0.0284131,
        'cubic_meters': 1000.0,
        'cubic_inches': 0.0163871,
        'cubic_feet': 28.3168,
    }
    source_unit_lower = source_unit.lower()
    target_unit_lower = target_unit.lower()
    if source_unit_lower not in conversion_rates:
        raise ValueError(f"Unsupported source unit: {source_unit}")
    if target_unit_lower not in conversion_rates:
        raise ValueError(f"Unsupported target unit: {target_unit}")
    try:
        numeric_value = float(value)
    except (TypeError, ValueError):
        raise ValueError(f"Invalid numeric value: {value}")
    if numeric_value < 0:
        raise ValueError(f"Volume cannot be negative: {value}")
    liters_value = numeric_value * conversion_rates[source_unit_lower]
    result = liters_value / conversion_rates[target_unit_lower]
    return result

if __name__ == '__main__':
    sample_value = 1.0
    sample_source = 'gallons_us'
    sample_target = 'liters'
    result = convert_volume(sample_value, sample_source, sample_target)
    print(result)
    sample_value_2 = 500
    sample_source_2 = 'milliliters'
    sample_target_2 = 'cups_us'
    result_2 = convert_volume(sample_value_2, sample_source_2, sample_target_2)
    print(result_2)
    sample_value_3 = 10
    sample_source_3 = 'cubic_meters'
    result_3 = convert_volume(sample_value_3, sample_source_3)
    print(result_3)