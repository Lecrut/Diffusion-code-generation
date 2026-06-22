VOLUME_CONSTANTS = {
    "L_ml": 1000.0,
    "L_L": 1.0,
    "m3_L": 1000.0,
    "m3_m3": 1.0,
    "gal_L": 3.78541,
    "gal_gal": 1.0,
    "ml_L": 0.001,
    "ml_ml": 0.001
}

def get_conversion_factor(from_unit, to_unit):
    if from_unit == to_unit:
        return 1.0
    
    key = f"{from_unit}_{to_unit}"
    
    if key in VOLUME_CONSTANTS:
        return VOLUME_CONSTANTS[key]
    
    to_base = f"{to_unit}_L"
    from_base = f"L_{from_unit}"
    
    if to_base in VOLUME_CONSTANTS and from_base in VOLUME_CONSTANTS:
        return VOLUME_CONSTANTS[to_base] / VOLUME_CONSTANTS[from_base]
    
    return 0.0

def convert_volume(value, from_unit, to_unit):
    factor = get_conversion_factor(from_unit, to_unit)
    return value * factor

if __name__ == '__main__':
    result_liters_to_milliliters = convert_volume(2.5, "L", "ml")
    print(result_liters_to_milliliters)
    
    result_cubic_meters_to_gallons = convert_volume(1.0, "m3", "gal")
    print(result_cubic_meters_to_gallons)