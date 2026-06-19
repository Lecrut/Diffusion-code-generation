def convert_volume_to_liters(volume, unit):
    conversion_factors = {
        'ml': 0.001,
        'cl': 0.01,
        'dl': 0.1,
        'l': 1.0,
        'gal': 3.785411784,
        'qt': 0.946352946,
        'pt': 0.473176473,
        'fl oz': 0.02957352956,
        'cup': 0.2365882365
    }
    
    if unit.lower() not in conversion_factors:
        raise ValueError("Unsupported unit")
    
    return volume * conversion_factors[unit.lower()]

if __name__ == '__main__':
    sample_volume = 10
    sample_unit = 'gal'
    converted_volume = convert_volume_to_liters(sample_volume, sample_unit)
    print(converted_volume)