def convert_to_liters(value, unit):
    conversion_factors = {
        "liter": 1.0,
        "litre": 1.0,
        "l": 1.0,
        "ml": 0.001,
        "milliliter": 0.001,
        "millilitre": 0.001,
        "cl": 0.01,
        "centiliter": 0.01,
        "centilitre": 0.01,
        "dl": 0.1,
        "deciliter": 0.1,
        "decilitre": 0.1,
        "m3": 1000.0,
        "cubic_meter": 1000.0,
        "cm3": 0.001,
        "cubic_centimeter": 0.001,
        "mm3": 1e-6,
        "cubic_millimeter": 1e-6,
        "us_fl_oz": 0.0295735295625,
        "us_fluid_ounce": 0.0295735295625,
        "us_cup": 0.2365882365,
        "us_pint": 0.473176473,
        "us_quart": 0.946352946,
        "us_gallon": 3.785411784,
        "uk_fl_oz": 0.0284130625,
        "uk_fluid_ounce": 0.0284130625,
        "uk_cup": 0.284130625,
        "uk_pint": 0.56826125,
        "uk_quart": 1.1365225,
        "uk_gallon": 4.54609,
        "tablespoon": 0.01478676478125,
        "teaspoon": 0.00492892159375,
        "barrel": 119.240471196,
        "bbl": 119.240471196,
        "tbsp": 0.01478676478125,
        "tsp": 0.00492892159375,
        "gallon": 3.785411784,
        "pint": 0.473176473,
        "quart": 0.946352946,
        "cup": 0.2365882365,
        "ounce": 0.0295735295625,
    }
    normalized_unit = unit.lower()
    if normalized_unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    return value * conversion_factors[normalized_unit]

if __name__ == '__main__':
    samples = [
        (1000, "ml"),
        (1, "liter"),
        (1, "us_gallon"),
        (1, "uk_gallon"),
        (1, "m3"),
        (16, "tablespoon"),
        (3, "cup"),
        (1, "barrel"),
    ]
    for value, unit in samples:
        result = convert_to_liters(value, unit)
        print(f"{value} {unit} = {result} liters")