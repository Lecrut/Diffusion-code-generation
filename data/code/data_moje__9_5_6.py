def convert_volume_to_liters(volume: float, unit: str) -> float:
    conversion_factors = {
        "liter": 1.0,
        "liters": 1.0,
        "l": 1.0,
        "milliliter": 0.001,
        "milliliters": 0.001,
        "ml": 0.001,
        "cubic_meter": 1000.0,
        "cubic_meters": 1000.0,
        "m3": 1000.0,
        "cubic_centimeter": 0.001,
        "cubic_centimeters": 0.001,
        "cm3": 0.001,
        "cubic_inch": 0.016387064,
        "cubic_inches": 0.016387064,
        "in3": 0.016387064,
        "cubic_foot": 28.316846592,
        "cubic_feet": 28.316846592,
        "ft3": 28.316846592,
        "gallon_us": 3.785411784,
        "gallons_us": 3.785411784,
        "gal_us": 3.785411784,
        "gallon_uk": 4.54609,
        "gallons_uk": 4.54609,
        "gal_uk": 4.54609,
        "quart_us": 0.946352946,
        "quarts_us": 0.946352946,
        "qt_us": 0.946352946,
        "quart_uk": 1.1365225,
        "quarts_uk": 1.1365225,
        "qt_uk": 1.1365225,
        "pint_us": 0.473176473,
        "pints_us": 0.473176473,
        "pt_us": 0.473176473,
        "pint_uk": 0.56826125,
        "pints_uk": 0.56826125,
        "pt_uk": 0.56826125,
        "cup_us": 0.2365882365,
        "cups_us": 0.2365882365,
        "tablespoon_us": 0.01478676478125,
        "tablespoons_us": 0.01478676478125,
        "teaspoon_us": 0.00492892159375,
        "teaspoons_us": 0.00492892159375,
    }
    normalized_unit = unit.lower()
    if normalized_unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    return volume * conversion_factors[normalized_unit]

if __name__ == "__main__":
    print(convert_volume_to_liters(1, "cubic_foot"))
    print(convert_volume_to_liters(5, "gallon_us"))
    print(convert_volume_to_liters(1000, "milliliters"))
    print(convert_volume_to_liters(2.5, "liter"))
    print(convert_volume_to_liters(100, "in3"))