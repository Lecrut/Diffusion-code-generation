conversion_factors = {
    "length": {
        "meter": 1.0,
        "kilometer": 1000.0,
        "mile": 1609.34,
        "foot": 0.3048,
        "inch": 0.0254
    },
    "mass": {
        "kilogram": 1.0,
        "gram": 0.001,
        "pound": 0.453592,
        "ounce": 0.0283495
    }
}
def convert(value, from_unit, to_unit, category):
    if category not in conversion_factors:
        raise ValueError("Invalid category")
    if from_unit not in conversion_factors[category] or to_unit not in conversion_factors[category]:
        raise ValueError("Invalid unit specified")
    if from_unit == to_unit:
        return value
    factor = 1.0
    if from_unit != to_unit:
        if category == "length":
            if from_unit in conversion_factors[category]:
                base_value = value * conversion_factors[category][from_unit]
                if to_unit in conversion_factors[category]:
                    return base_value / conversion_factors[category][to_unit]
        elif category == "mass":
            if from_unit in conversion_factors[category]:
                base_value = value * conversion_factors[category][from_unit]
                if to_unit in conversion_factors[category]:
                    return base_value / conversion_factors[category][to_unit]
    raise NotImplementedError("Conversion not implemented for this pair")
if __name__ == '__main__':
    print("--- Length Conversion ---")
    length_value = 10
    from_unit = "meter"
    to_unit = "kilometer"
    category = "length"
    try:
        result = convert(length_value, from_unit, to_unit, category)
        print(f"{length_value} {from_unit} is equal to {result} {to_unit}")
    except Exception as e:
        print(f"Error during length conversion: {e}")
    print("\n--- Mass Conversion ---")
    mass_value = 5
    from_unit = "kilogram"
    to_unit = "pound"
    category = "mass"
    try:
        result = convert(mass_value, from_unit, to_unit, category)
        print(f"{mass_value} {from_unit} is equal to {result} {to_unit}")
    except Exception as e:
        print(f"Error during mass conversion: {e}")
    print("\n--- Bidirectional Check (Mile to Foot) ---")
    length_value = 1
    from_unit = "mile"
    to_unit = "foot"
    category = "length"
    try:
        result = convert(length_value, from_unit, to_unit, category)
        print(f"{length_value} {from_unit} is equal to {result} {to_unit}")
    except Exception as e:
        print(f"Error during bidirectional length conversion: {e}")