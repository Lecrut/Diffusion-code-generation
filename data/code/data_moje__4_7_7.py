def normalize_to_meters(distance_value, distance_unit):
    unit_map = {
        "meter": 1.0,
        "metre": 1.0,
        "m": 1.0,
        "meters": 1.0,
        "metres": 1.0,
        "kilometer": 1000.0,
        "kilometre": 1000.0,
        "km": 1000.0,
        "kilometers": 1000.0,
        "kilometres": 1000.0,
        "centimeter": 0.01,
        "centimetre": 0.01,
        "cm": 0.01,
        "centimeters": 0.01,
        "centimetres": 0.01,
        "millimeter": 0.001,
        "millimetre": 0.001,
        "mm": 0.001,
        "millimeters": 0.001,
        "millimetres": 0.001,
        "micrometer": 1e-6,
        "micrometre": 1e-6,
        "um": 1e-6,
        "micron": 1e-6,
        "nanometer": 1e-9,
        "nanometre": 1e-9,
        "nm": 1e-9,
        "inch": 0.0254,
        "in": 0.0254,
        "inches": 0.0254,
        "foot": 0.3048,
        "ft": 0.3048,
        "feet": 0.3048,
        "yard": 0.9144,
        "yd": 0.9144,
        "yards": 0.9144,
        "mile": 1609.344,
        "mi": 1609.344,
        "miles": 1609.344,
        "nautical_mile": 1852.0,
        "nm": 1852.0,
        "nmile": 1852.0,
        "nmi": 1852.0,
        "knot": 1852.0 / 3600.0,
    }
    
    cleaned_unit = distance_unit.lower().strip()
    
    if cleaned_unit not in unit_map:
        raise ValueError("Unknown unit: {}".format(distance_unit))
        
    factor = unit_map[cleaned_unit]
    return distance_value * factor

if __name__ == '__main__':
    samples = [
        (1.0, "km"),
        (100.0, "cm"),
        (1.0, "mi"),
        (12.0, "in"),
        (1.0, "yard"),
        (1000.0, "mm"),
        (1.0, "nautical_mile"),
    ]
    
    results = []
    for val, unit in samples:
        converted = normalize_to_meters(val, unit)
        results.append(converted)
        
    for res in results:
        print(res)