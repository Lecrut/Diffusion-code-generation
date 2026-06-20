def convert_length(value, from_unit, to_unit):
    units_to_meters = {
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

    from_unit_lower = from_unit.lower().replace("-", "_").replace(" ", "_")
    to_unit_lower = to_unit.lower().replace("-", "_").replace(" ", "_")

    if from_unit_lower not in units_to_meters:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit_lower not in units_to_meters:
        raise ValueError(f"Unsupported target unit: {to_unit}")

    meters = value * units_to_meters[from_unit_lower]
    result = meters / units_to_meters[to_unit_lower]
    return result

if __name__ == "__main__":
    sample_value = 12.0
    source = "feet"
    target = "meters"
    converted = convert_length(sample_value, source, target)
    print(converted)