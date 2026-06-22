def convert_volume(volume, source_unit, target_unit="liters"):
    if not isinstance(volume, (int, float)):
        raise ValueError("Volume must be a number")
    if volume < 0:
        raise ValueError("Volume cannot be negative")

    conversion_to_liters = {
        "liters": 1.0,
        "milliliters": 0.001,
        "gallons": 3.78541,
        "quarts": 0.946353,
        "pints": 0.473176,
        "cups": 0.24,
        "fluid_ounces": 0.0295735,
        "tablespoons": 0.0147868,
        "teaspoons": 0.00492892,
        "cubic_meters": 1000.0,
        "cubic_inches": 0.0163871,
        "cubic_feet": 28.3168,
    }

    source_unit_lower = source_unit.lower()
    target_unit_lower = target_unit.lower()

    if source_unit_lower not in conversion_to_liters:
        raise ValueError(f"Unsupported source unit: {source_unit}")
    if target_unit_lower not in conversion_to_liters:
        raise ValueError(f"Unsupported target unit: {target_unit}")

    volume_in_liters = volume * conversion_to_liters[source_unit_lower]
    result = volume_in_liters / conversion_to_liters[target_unit_lower]

    return result

if __name__ == "__main__":
    print(convert_volume(1, "gallons", "liters"))
    print(convert_volume(500, "milliliters", "cups"))
    print(convert_volume(2, "cubic_feet", "liters"))
    print(convert_volume(10, "cups", "fluid_ounces"))
    try:
        convert_volume(-5, "liters", "gallons")
    except ValueError as e:
        print(e)
    try:
        convert_volume(10, "invalid_unit", "liters")
    except ValueError as e:
        print(e)