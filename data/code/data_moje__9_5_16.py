LITER_FACTORS = {
    "l": 1.0,
    "liter": 1.0,
    "liters": 1.0,
    "ml": 0.001,
    "milliliter": 0.001,
    "milliliters": 0.001,
    "us_gal": 3.785411784,
    "us_gallon": 3.785411784,
    "us_gallons": 3.785411784,
    "us_qt": 0.946352946,
    "us_quart": 0.946352946,
    "us_quarts": 0.946352946,
    "us_pt": 0.473176473,
    "us_pint": 0.473176473,
    "us_pints": 0.473176473,
    "us_fl_oz": 0.0295735295625,
    "us_fluid_ounce": 0.0295735295625,
    "us_fluid_ounces": 0.0295735295625,
    "uk_gal": 4.54609,
    "uk_gallon": 4.54609,
    "uk_gallons": 4.54609,
    "uk_qt": 1.1365225,
    "uk_quart": 1.1365225,
    "uk_quarts": 1.1365225,
    "uk_pt": 0.56826125,
    "uk_pint": 0.56826125,
    "uk_pints": 0.56826125,
    "uk_fl_oz": 0.0284130625,
    "uk_fluid_ounce": 0.0284130625,
    "uk_fluid_ounces": 0.0284130625,
    "m3": 1000.0,
    "cubic_meter": 1000.0,
    "cubic_meters": 1000.0,
    "dm3": 1.0,
    "cubic_decimeter": 1.0,
    "cubic_decimeters": 1.0,
    "cm3": 0.001,
    "cubic_centimeter": 0.001,
    "cubic_centimeters": 0.001,
    "in3": 0.016387064,
    "cubic_inch": 0.016387064,
    "cubic_inches": 0.016387064,
    "ft3": 28.316846592,
    "cubic_foot": 28.316846592,
    "cubic_feet": 28.316846592,
    "bbl": 158.987294928,
    "oil_barrel": 158.987294928,
    "oil_barrels": 158.987294928,
    "drop": 0.00005,
}

def convert_volume_to_liters(value, unit):
    normalized_unit = str(unit).strip().lower()
    if normalized_unit not in LITER_FACTORS:
        raise ValueError(f"Unsupported unit: {unit}")
    factor = LITER_FACTORS[normalized_unit]
    return value * factor

if __name__ == '__main__':
    samples = [
        (100, "ml"),
        (1, "us_gal"),
        (1, "uk_gal"),
        (5, "ft3"),
        (1000, "cm3"),
        (2.5, "us_gallons"),
        (0.5, "bbl"),
    ]
    for val, u in samples:
        result = convert_volume_to_liters(val, u)
        print(f"{val} {u} = {result} liters")