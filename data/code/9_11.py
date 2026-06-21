def convert_volume(volume, source_unit, target_unit=None):
    if target_unit is None:
        target_unit = source_unit

    units_to_liters = {
        'ml': 0.001,
        'milliliter': 0.001,
        'l': 1.0,
        'liter': 1.0,
        'gal': 3.78541,
        'gallon': 3.78541,
        'qt': 0.946353,
        'quart': 0.946353,
        'pt': 0.473176,
        'pint': 0.473176,
        'cup': 0.236588,
        'fl_oz': 0.0295735,
        'fluid_ounce': 0.0295735,
        'tbsp': 0.0147868,
        'tablespoon': 0.0147868,
        'tsp': 0.00492892,
        'teaspoon': 0.00492892,
        'm3': 1000.0,
        'cubic_meter': 1000.0,
        'ft3': 0.0283168,
        'cubic_foot': 0.0283168,
        'in3': 0.0000163871,
        'cubic_inch': 0.0000163871,
    }

    src_lower = source_unit.lower()
    tgt_lower = target_unit.lower()

    if src_lower not in units_to_liters:
        raise ValueError(f"Unknown source unit: {source_unit}")
    if tgt_lower not in units_to_liters:
        raise ValueError(f"Unknown target unit: {target_unit}")

    liters = volume * units_to_liters[src_lower]
    result_liters = liters / units_to_liters[tgt_lower]

    return result_liters

if __name__ == '__main__':
    val = convert_volume(1000, 'ml', 'l')
    print(val)
    val2 = convert_volume(1, 'gal', 'l')
    print(val2)
    val3 = convert_volume(1, 'l', 'l')
    print(val3)