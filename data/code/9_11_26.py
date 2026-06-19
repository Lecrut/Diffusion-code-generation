def convert_volume(volume, source_unit, target_unit='liter'):
    conversion_rates = {
        'liter': {'liter': 1, 'milliliter': 1000, 'gallon': 0.264172},
        'milliliter': {'liter': 0.001, 'milliliter': 1, 'gallon': 0.000264172},
        'gallon': {'liter': 3.78541, 'milliliter': 3785.41, 'gallon': 1}
    }
    
    if source_unit not in conversion_rates or target_unit not in conversion_rates[source_unit]:
        return "Invalid unit(s)"
    
    conversion_factor = conversion_rates[source_unit][target_unit]
    converted_volume = volume * conversion_factor
    return converted_volume

if __name__ == '__main__':
    sample_volume = 5.0
    source_unit = 'liter'
    target_unit = 'gallon'
    
    result = convert_volume(sample_volume, source_unit, target_unit)
    print(result)