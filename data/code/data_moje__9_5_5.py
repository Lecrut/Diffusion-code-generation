def convert_volume_to_liters(value: float, unit: str) -> float:
    conversion_factors = {
        "liter": 1.0,
        "l": 1.0,
        "L": 1.0,
        "milliliter": 0.001,
        "ml": 0.001,
        "mL": 0.001,
        "gallon_us": 3.785411784,
        "gal_us": 3.785411784,
        "quart_us": 0.946352946,
        "qt_us": 0.946352946,
        "pint_us": 0.473176473,
        "pt_us": 0.473176473,
        "cup_us": 0.2365882365,
        "fluid_ounce_us": 0.0295735295625,
        "fl_oz_us": 0.0295735295625,
        "gallon_uk": 4.54609,
        "gal_uk": 4.54609,
        "quart_uk": 1.1365225,
        "qt_uk": 1.1365225,
        "pint_uk": 0.56826125,
        "pt_uk": 0.56826125,
        "cup_uk": 0.284130625,
        "fluid_ounce_uk": 0.0284130625,
        "fl_oz_uk": 0.0284130625,
        "cubic_meter": 1000.0,
        "m3": 1000.0,
        "cubic_centimeter": 0.001,
        "cm3": 0.001,
        "cc": 0.001,
        "cubic_foot": 28.316846592,
        "ft3": 28.316846592,
        "cubic_inch": 0.016387064,
        "in3": 0.016387064,
        "tablespoon_us": 0.01478676478125,
        "tbsp_us": 0.01478676478125,
        "teaspoon_us": 0.00492892159375,
        "tsp_us": 0.00492892159375,
    }
    normalized_unit = unit.lower().replace("_", "").replace("-", "").replace(" ", "")
    lookup_key = unit.lower()
    if lookup_key in conversion_factors:
        return value * conversion_factors[lookup_key]
    for key, factor in conversion_factors.items():
        if key.lower().replace("_", "").replace("-", "").replace(" ", "") == normalized_unit:
            return value * factor
    raise ValueError(f"Unsupported unit: {unit}")

if __name__ == '__main__':
    sample_values = [
        (1, "gallon_us"),
        (2, "quart_uk"),
        (500, "ml"),
        (1, "cubic_meter"),
        (16, "fluid_ounce_us"),
        (0.5, "gallon_uk"),
        (100, "tbsp_us"),
    ]
    for value, unit in sample_values:
        result = convert_volume_to_liters(value, unit)
        print(f"{value} {unit} = {result} liters")