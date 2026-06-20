def convert_volume(volume, target_unit):
    _to_liters = {
        'm3': 1000.0,
        'L': 1.0,
        'mL': 0.001,
        'gal': 3.78541,
        'qt': 0.946353,
        'pt': 0.473176,
        'cup': 0.236588,
        'fl_oz': 0.0295735,
    }
    
    if target_unit not in _to_liters:
        raise ValueError(f"Unsupported unit: {target_unit}")
    
    liters = volume * _to_liters[target_unit]
    return liters / 1.0

if __name__ == '__main__':
    result = convert_volume(5, 'gal')
    print(result)
    
    result_m3 = convert_volume(2000, 'mL')
    print(result_m3)
    
    result_cups = convert_volume(1, 'm3')
    print(result_cups)