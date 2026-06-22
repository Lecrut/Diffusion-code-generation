CONVERSION_TO_METERS = {
    "meter": 1.0,
    "m": 1.0,
    "kilometer": 1000.0,
    "km": 1000.0,
    "centimeter": 0.01,
    "cm": 0.01,
    "millimeter": 0.001,
    "mm": 0.001,
    "micrometer": 1e-6,
    "um": 1e-6,
    "nanometer": 1e-9,
    "nm": 1e-9,
    "inch": 0.0254,
    "in": 0.0254,
    "foot": 0.3048,
    "ft": 0.3048,
    "yard": 0.9144,
    "yd": 0.9144,
    "mile": 1609.344,
    "mi": 1609.344,
    "nautical_mile": 1852.0,
    "nmi": 1852.0,
}

def convert_length(value, source_unit, target_unit):
    source_unit = source_unit.lower()
    target_unit = target_unit.lower()
    
    if source_unit not in CONVERSION_TO_METERS:
        raise ValueError(f"Unsupported source unit: {source_unit}")
    if target_unit not in CONVERSION_TO_METERS:
        raise ValueError(f"Unsupported target unit: {target_unit}")
    
    meters = value * CONVERSION_TO_METERS[source_unit]
    result = meters / CONVERSION_TO_METERS[target_unit]
    return result

if __name__ == '__main__':
    print(convert_length(5, "feet", "meters"))
    print(convert_length(1, "mile", "kilometers"))
    print(convert_length(100, "cm", "m"))
    print(convert_length(12, "inches", "feet"))