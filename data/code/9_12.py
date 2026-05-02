def convert_volume(volume, source_unit, target_unit=None):
    conversion_rates = {
        "liter": 1.0,
        "milliliter": 0.001,
        "gallon": 3.78541,
        "quart": 0.946353,
        "ounce": 0.0283495,
        "cubic_meter": 1000.0,
        "cubic_foot": 28.3168,
    }
    if source_unit not in conversion_rates:
        raise ValueError(f"Unknown source unit: {source_unit}")
    if target_unit is None:
        return volume
    if target_unit not in conversion_rates:
        raise ValueError(f"Unknown target unit: {target_unit}")
    if source_unit == target_unit:
        return volume
    base_volume = volume * conversion_rates[source_unit]
    if target_unit == "liter":
        return base_volume
    if target_unit == "cubic_meter":
        return base_volume / 1000.0
    if target_unit == "cubic_foot":
        return base_volume / 28.3168
    return base_volume
if __name__ == '__main__':
    print(convert_volume(10, "liter"))
    print(convert_volume(1, "gallon", "liter"))
    print(convert_volume(500, "milliliter", "liter"))
    print(convert_volume(1, "cubic_meter", "gallon"))
    try:
        convert_volume(10, "furlong", "meter")
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        convert_volume(10, "liter", "furlong")
    except ValueError as e:
        print(f"Error caught: {e}")