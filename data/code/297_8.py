import math
def convert_units_iterative(value, source_unit, target_unit):
    if source_unit == target_unit:
        return value
    conversion_factors = {}
    if source_unit == "meter":
        conversion_factors["meter"] = 1.0
        if target_unit == "kilometer":
            conversion_factors["kilometer"] = 1 / 1000.0
        elif target_unit == "centimeter":
            conversion_factors["centimeter"] = 1000.0
    elif source_unit == "liter":
        conversion_factors["liter"] = 1.0
        if target_unit == "milliliter":
            conversion_factors["milliliter"] = 1000.0
    elif source_unit == "gram":
        conversion_factors["gram"] = 1.0
        if target_unit == "kilogram":
            conversion_factors["kilogram"] = 1 / 1000.0
        elif target_unit == "milligram":
            conversion_factors["milligram"] = 1000.0
    if source_unit in conversion_factors and target_unit in conversion_factors:
        factor_from_source = conversion_factors[source_unit]
        factor_to_target = conversion_factors[target_unit]
        result = value * factor_from_source / factor_to_target
        return result
    else:
        raise ValueError(f"Unsupported unit conversion: {source_unit} to {target_unit}")
if __name__ == '__main__':
    value = 500.0
    source = "meter"
    target = "kilometer"
    result1 = convert_units_iterative(value, source, target)
    print(f"{value} {source} is equal to {result1} {target}")
    value = 2.5
    source = "liter"
    target = "milliliter"
    result2 = convert_units_iterative(value, source, target)
    print(f"{value} {source} is equal to {result2} {target}")
    value = 1000.0
    source = "gram"
    target = "kilogram"
    result3 = convert_units_iterative(value, source, target)
    print(f"{value} {source} is equal to {result3} {target}")
    try:
        convert_units_iterative(10, "meter", "second")
    except ValueError as e:
        print(f"Error caught: {e}")