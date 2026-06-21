def convert_volume(volume, source_unit, target_unit="liters"):
    conversion_to_base = {
        "liters": 1.0,
        "milliliters": 0.001,
        "gallons": 3.78541,
        "quarts": 0.946353,
        "pints": 0.473176,
        "cups": 0.236588,
        "fluid_ounces": 0.0295735,
        "tablespoons": 0.0147868,
        "teaspoons": 0.00492892,
        "cubic_meters": 1000.0,
        "cubic_centimeters": 0.001,
        "cubic_inches": 0.0163871
    }

    if not isinstance(volume, (int, float)):
        raise ValueError("Volume must be a number")

    if volume < 0:
        raise ValueError("Volume cannot be negative")

    source_unit_lower = source_unit.lower()
    target_unit_lower = target_unit.lower()

    if source_unit_lower not in conversion_to_base:
        raise ValueError(f"Unsupported source unit: {source_unit}")

    if target_unit_lower not in conversion_to_base:
        raise ValueError(f"Unsupported target unit: {target_unit}")

    base_volume = volume * conversion_to_base[source_unit_lower]
    converted_volume = base_volume / conversion_to_base[target_unit_lower]

    return converted_volume

if __name__ == '__main__':
    result1 = convert_volume(1, "gallons")
    print(result1)

    result2 = convert_volume(500, "milliliters", "cups")
    print(result2)

    result3 = convert_volume(10, "cubic_inches", "liters")
    print(result3)