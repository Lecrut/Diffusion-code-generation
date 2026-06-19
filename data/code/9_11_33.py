def convert_volume(volume, source_unit, target_unit='liter'):
    conversion_rates = {
        'liter': {'liter': 1, 'milliliter': 1000, 'gallon': 0.264172},
        'milliliter': {'liter': 0.001, 'milliliter': 1, 'gallon': 0.000264172},
        'gallon': {'liter': 3.78541, 'milliliter': 3785.41, 'gallon': 1}
    }
    
    if source_unit not in conversion_rates:
        raise ValueError(f"Unsupported source unit: {source_unit}")
    if target_unit not in conversion_rates[source_unit]:
        raise ValueError(f"Unsupported target unit: {target_unit}")
    
    return volume * conversion_rates[source_unit][target_unit]

if __name__ == '__main__':
    try:
        print(convert_volume(10, 'liter', 'gallon'))
        print(convert_volume(500, 'milliliter', 'liter'))
        print(convert_volume(2, 'gallon', 'milliliter'))
    except ValueError as e:
        print(e)