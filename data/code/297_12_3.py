def convert_quantity(conversion_factors, quantity, source_unit, target_unit):
    if source_unit == target_unit:
        return quantity
    for conversion_type, factors in conversion_factors.items():
        if conversion_type == f"{source_unit}_to_{target_unit}":
            if "base" in factors and factors["base"] != 0:
                result = quantity * (factors["value"] / factors["base"])
                return result
    raise ValueError(f"No conversion factor found for {source_unit} to {target_unit}")
if __name__ == '__main__':
    conversion_data = {
        "length": {
            "meter_to_foot": {"base": 3.28084, "value": 1},
            "foot_to_meter": {"base": 3.28084, "value": 1/3.28084}
        },
        "mass": {
            "kilogram_to_pound": {"base": 2.20462, "value": 1},
            "pound_to_kilogram": {"base": 2.20462, "value": 1/2.20462}
        },
        "volume": {
            "liter_to_gallon": {"base": 3.78541, "value": 1},
            "gallon_to_liter": {"base": 3.78541, "value": 1/3.78541}
        }
    }
    input_quantity = 10
    source = "meter"
    target = "foot"
    try:
        result = convert_quantity(conversion_data, input_quantity, source, target)
        print(f"{input_quantity} {source} is equal to {result} {target}")
    except ValueError as e:
        print(e)
    input_quantity = 5
    source = "kilogram"
    target = "pound"
    try:
        result = convert_quantity(conversion_data, input_quantity, source, target)
        print(f"{input_quantity} {source} is equal to {result} {target}")
    except ValueError as e:
        print(e)
    input_quantity = 10
    source = "liter"
    target = "gallon"
    try:
        result = convert_quantity(conversion_data, input_quantity, source, target)
        print(f"{input_quantity} {source} is equal to {result} {target}")
    except ValueError as e:
        print(e)