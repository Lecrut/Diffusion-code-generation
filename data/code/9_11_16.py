def convert_volume(volume, source_unit, target_unit="liters"):
    conversion_rates = {
        "liters": 1.0,
        "milliliters": 0.001,
        "cubic_meters": 1000.0,
        "gallons": 3.78541,
        "quarts": 0.946353,
        "pints": 0.473176,
        "cups": 0.236588,
        "fluid_ounces": 0.0295735,
        "tablespoons": 0.0147868,
        "teaspoons": 0.00492892,
        "cubic_inches": 0.0163871,
        "cubic_feet": 28.3168,
        "cubic_yards": 764.555,
        "barrels": 158.987,
    }

    source_lower = source_unit.lower()
    target_lower = target_unit.lower()

    if source_lower not in conversion_rates:
        raise ValueError(f"Unsupported source unit: {source_unit}")
    if target_lower not in conversion_rates:
        raise ValueError(f"Unsupported target unit: {target_unit}")

    if not isinstance(volume, (int, float)):
        raise TypeError("Volume must be a numeric value")

    volume_in_liters = volume * conversion_rates[source_lower]
    result = volume_in_liters / conversion_rates[target_lower]

    return result

if __name__ == '__main__':
    print(convert_volume(1, "gallons", "liters"))
    print(convert_volume(1000, "milliliters", "liters"))
    print(convert_volume(1, "cubic_feet", "cubic_inches"))
    print(convert_volume(5, "liters", "gallons"))