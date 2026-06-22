def convert_volume(volume, source_unit, target_unit=None):
    if target_unit is None:
        target_unit = source_unit
    
    if not isinstance(volume, (int, float)):
        raise ValueError("Volume must be a number")
    
    if not isinstance(source_unit, str) or not isinstance(target_unit, str):
        raise ValueError("Units must be strings")
        
    source_unit = source_unit.lower().strip()
    target_unit = target_unit.lower().strip()
    
    conversions_to_liters = {
        'liter': 1.0,
        'litre': 1.0,
        'l': 1.0,
        'milliliter': 0.001,
        'millilitre': 0.001,
        'ml': 0.001,
        'gallon': 3.78541,
        'gal': 3.78541,
        'quart': 0.946353,
        'qt': 0.946353,
        'pint': 0.473176,
        'pt': 0.473176,
        'cup': 0.236588,
        'cup_us': 0.236588,
        'fluid_ounce': 0.0295735,
        'fl_oz': 0.0295735,
        'cubic_meter': 1000.0,
        'm3': 1000.0,
        'cubic_centimeter': 0.001,
        'cc': 0.001,
        'cm3': 0.001,
        'cubic_inch': 0.0163871,
        'in3': 0.0163871,
        'cubic_foot': 28.3168,
        'ft3': 28.3168,
    }
    
    if source_unit not in conversions_to_liters:
        raise ValueError(f"Unknown source unit: {source_unit}")
    if target_unit not in conversions_to_liters:
        raise ValueError(f"Unknown target unit: {target_unit}")
        
    if source_unit == target_unit:
        return volume
        
    volume_in_liters = volume * conversions_to_liters[source_unit]
    converted_volume = volume_in_liters / conversions_to_liters[target_unit]
    
    return converted_volume

if __name__ == '__main__':
    result = convert_volume(1, 'gallon', 'liter')
    print(result)