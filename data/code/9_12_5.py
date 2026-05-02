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
    base_unit = "liter"
    if source_unit != base_unit:
        source_rate = conversion_rates[source_unit]
        volume_in_liters = volume / source_rate
    else:
        volume_in_liters = volume
    target_rate = conversion_rates[target_unit]
    result = volume_in_liters * target_rate
    return result
if __name__ == '__main__':
    print(convert_volume(10, "liter"))
    print(convert_volume(1, "gallon", "liter"))
    print(convert_volume(5, "cubic_meter", "liter"))
    print(convert_volume(100, "milliliter", "liter"))
    print(convert_volume(1, "ounce", "gallon"))
    try:
        convert_volume(10, "furlong", "meter")
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        convert_volume(10, "liter", "furlong")
    except ValueError as e:
        print(f"Error caught: {e}")