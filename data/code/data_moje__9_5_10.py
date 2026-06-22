def convert_to_liters(volume, unit):
    conversion_factors = {
        "liter": 1.0,
        "l": 1.0,
        "L": 1.0,
        "milliliter": 0.001,
        "ml": 0.001,
        "mL": 0.001,
        "gallon_us": 3.785411784,
        "gallon_uk": 4.54609,
        "gal_us": 3.785411784,
        "gal_uk": 4.54609,
        "quart_us": 0.946352946,
        "quart_uk": 1.1365225,
        "qt_us": 0.946352946,
        "qt_uk": 1.1365225,
        "pint_us": 0.473176473,
        "pint_uk": 0.56826125,
        "pt_us": 0.473176473,
        "pt_uk": 0.56826125,
        "cup_us": 0.2365882365,
        "cup_uk": 0.284130625,
        "tablespoon_us": 0.01478676478,
        "tbsp_us": 0.01478676478,
        "teaspoon_us": 0.00492892159,
        "tsp_us": 0.00492892159,
        "cubic_meter": 1000.0,
        "m3": 1000.0,
        "cubic_centimeter": 0.001,
        "cm3": 0.001,
        "cc": 0.001,
        "cubic_inch": 0.016387064,
        "in3": 0.016387064,
        "cubic_foot": 28.316846592,
        "ft3": 28.316846592,
        "cubic_yard": 764.554857984,
        "yd3": 764.554857984,
        "barrel_oil": 158.987294928,
        "bbl": 158.987294928,
    }
    
    unit_key = unit.lower().replace(" ", "_").replace("-", "_")
    
    if unit_key not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    
    factor = conversion_factors[unit_key]
    return volume * factor

if __name__ == '__main__':
    result1 = convert_to_liters(5, "gallon_us")
    print(result1)
    result2 = convert_to_liters(1000, "milliliter")
    print(result2)
    result3 = convert_to_liters(2, "cubic_foot")
    print(result3)
    result4 = convert_to_liters(1, "liter")
    print(result4)
    result5 = convert_to_liters(3.5, "cup_us")
    print(result5)