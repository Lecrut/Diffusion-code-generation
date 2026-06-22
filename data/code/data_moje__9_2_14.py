VOLUME_CONVERSION_TO_LITERS = {
    'L': 1.0,
    'l': 1.0,
    'ml': 0.001,
    'mL': 0.001,
    'm3': 1000.0,
    'm³': 1000.0,
    'gal': 3.78541,
    'qt': 0.946353,
    'pt': 0.473176,
    'fl_oz': 0.0295735,
    'in3': 0.0163871,
    'ft3': 28.3168,
}

def convert_volume(value, target_unit):
    if target_unit not in VOLUME_CONVERSION_TO_LITERS:
        raise ValueError(f"Unsupported unit: {target_unit}")
    
    liters = value * VOLUME_CONVERSION_TO_LITERS[target_unit]
    
    if target_unit == 'L' or target_unit == 'l':
        return liters
    
    if target_unit == 'm3' or target_unit == 'm³':
        return liters / 1000.0
    
    if target_unit == 'ml' or target_unit == 'mL':
        return liters * 1000.0
    
    if target_unit == 'gal':
        return liters / VOLUME_CONVERSION_TO_LITERS['gal']
    
    if target_unit == 'qt':
        return liters / VOLUME_CONVERSION_TO_LITERS['qt']
    
    if target_unit == 'pt':
        return liters / VOLUME_CONVERSION_TO_LITERS['pt']
    
    if target_unit == 'fl_oz':
        return liters / VOLUME_CONVERSION_TO_LITERS['fl_oz']
    
    if target_unit == 'in3':
        return liters / VOLUME_CONVERSION_TO_LITERS['in3']
    
    if target_unit == 'ft3':
        return liters / VOLUME_CONVERSION_TO_LITERS['ft3']
    
    return liters

if __name__ == '__main__':
    sample_value = 50
    sample_unit = 'gal'
    result = convert_volume(sample_value, sample_unit)
    print(f"{sample_value} {sample_unit} = {result} L")
    
    sample_value_2 = 1000
    sample_unit_2 = 'm3'
    result_2 = convert_volume(sample_value_2, sample_unit_2)
    print(f"{sample_value_2} {sample_unit_2} = {result_2} L")
    
    sample_value_3 = 1
    sample_unit_3 = 'L'
    result_3 = convert_volume(sample_value_3, sample_unit_3)
    print(f"{sample_value_3} {sample_unit_3} = {result_3} L")
    
    sample_value_4 = 1
    sample_unit_4 = 'gal'
    result_4 = convert_volume(sample_value_4, sample_unit_4)
    print(f"{sample_value_4} {sample_unit_4} = {result_4} L")