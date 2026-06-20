import math

VOLUME_CONVERSION_FACTORS = {
    'liter': 1.0,
    'milliliter': 0.001,
    'cubic_meter': 1000.0,
    'gallon': 3.785411784,
    'cubic_inch': 0.016387064,
}

VALID_UNITS = set(VOLUME_CONVERSION_FACTORS.keys())

def convert_volume(value, from_unit, to_unit):
    if from_unit not in VALID_UNITS:
        raise ValueError(f"Invalid source unit: {from_unit}")
    if to_unit not in VALID_UNITS:
        raise ValueError(f"Invalid target unit: {to_unit}")
    
    liters = value * VOLUME_CONVERSION_FACTORS[from_unit]
    converted_value = liters / VOLUME_CONVERSION_FACTORS[to_unit]
    
    return converted_value

if __name__ == '__main__':
    result_liters_to_gallons = convert_volume(10, 'liter', 'gallon')
    print(f"10 liters is {result_liters_to_gallons} gallons")
    
    result_milliliters_to_cubic_meters = convert_volume(500000, 'milliliter', 'cubic_meter')
    print(f"500000 milliliters is {result_milliliters_to_cubic_meters} cubic meters")
    
    result_gallons_to_liters = convert_volume(1, 'gallon', 'liter')
    print(f"1 gallon is {result_gallons_to_liters} liters")
    
    result_cubic_inches_to_liters = convert_volume(61.0237441, 'cubic_inch', 'liter')
    print(f"61.0237441 cubic inches is {result_cubic_inches_to_liters} liters")
    
    result_liters_to_cubic_inches = convert_volume(1, 'liter', 'cubic_inch')
    print(f"1 liter is {result_liters_to_cubic_inches} cubic inches")