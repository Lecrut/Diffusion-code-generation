def convert_volume(volume, source_unit, target_unit="liter"):
    if not isinstance(volume, (int, float)):
        raise TypeError("Volume must be a number")
    if volume < 0:
        raise ValueError("Volume cannot be negative")

    conversion_to_liters = {
        "liter": 1.0,
        "milliliter": 0.001,
        "gallon": 3.78541,
        "quart": 0.946353,
        "pint": 0.473176,
        "cup": 0.236588,
        "fluid_ounce": 0.0295735,
        "tablespoon": 0.0147868,
        "teaspoon": 0.00492892,
        "cubic_meter": 1000.0,
        "cubic_centimeter": 0.001,
        "cubic_inch": 0.0163871
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

if __name__ == '__main__':
    print(convert_volume(1, "gallon", "liter"))
    print(convert_volume(500, "milliliter", "cup"))
    print(convert_volume(2.5, "liter", "gallon"))