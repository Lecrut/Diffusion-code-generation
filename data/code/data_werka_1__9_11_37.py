def convert_volume(volume, source_unit, target_unit='liters'):
    conversion_rates = {
        'liters': {'milliliters': 1000, 'cubic_meters': 0.001, 'gallons': 0.264172},
        'milliliters': {'liters': 0.001, 'cubic_meters': 0.000001, 'gallons': 0.000264172},
        'cubic_meters': {'liters': 1000, 'milliliters': 1000000, 'gallons': 264.172},
        'gallons': {'liters': 3.78541, 'milliliters': 3785.41, 'cubic_meters': 0.00378541}
    }
    
    if source_unit not in conversion_rates:
        raise ValueError(f"Unsupported source unit: {source_unit}")
    if target_unit not in conversion_rates[source_unit]:
        raise ValueError(f"Unsupported target unit: {target_unit} from source unit: {source_unit}")
    
    return volume * conversion_rates[source_unit][target_unit]

if __name__ == '__main__':
    try:
        print(convert_volume(1, 'liters', 'gallons'))
        print(convert_volume(500, 'milliliters', 'cubic_meters'))
        print(convert_volume(2, 'gallons', 'liters'))
    except ValueError as e:
        print(e)