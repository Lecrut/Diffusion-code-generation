UNIT_FACTORS = {
    'meters': 1.0,
    'kilometers': 1000.0,
    'centimeters': 0.01,
    'millimeters': 0.001,
    'inches': 0.0254,
    'feet': 0.3048,
    'yards': 0.9144,
    'miles': 1609.344
}

def convert_length(value, from_unit, to_unit):
    if from_unit not in UNIT_FACTORS:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit not in UNIT_FACTORS:
        raise ValueError(f"Unsupported target unit: {to_unit}")
    
    meters_value = value * UNIT_FACTORS[from_unit]
    result = meters_value / UNIT_FACTORS[to_unit]
    return result

if __name__ == '__main__':
    print(convert_length(1, 'meters', 'feet'))
    print(convert_length(1, 'kilometers', 'miles'))
    print(convert_length(1, 'inches', 'centimeters'))
    print(convert_length(10, 'yards', 'meters'))
    print(convert_length(100, 'millimeters', 'inches'))