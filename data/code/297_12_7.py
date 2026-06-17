def convert_quantity(conversion_factors, quantity, source_unit, target_unit):
    if source_unit == target_unit:
        return quantity
    for factor_type, factors in conversion_factors.items():
        if factor_type in factors and source_unit in factors[factor_type] and target_unit in factors[factor_type]:
            try:
                if source_unit == target_unit:
                    return quantity
                if (source_unit, target_unit) in factors[factor_type]:
                    return quantity * factors[factor_type][(source_unit, target_unit)]
            except KeyError:
                continue
    return None
if __name__ == '__main__':
    conversion_data = {
        "length": {
            ("meter", "foot"): 3.28084,
            ("inch", "meter"): 0.0254
        },
        "mass": {
            ("kilogram", "pound"): 2.20462
        },
        "volume": {
            ("liter", "gallon_us"): 3.78541
        }
    }
    input_quantity = 10
    print(f"Input Quantity: {input_quantity}")
    source1 = "meter"
    target1 = "foot"
    result1 = convert_quantity(conversion_data, input_quantity, source1, target1)
    print(f"{input_quantity} {source1} is equal to {result1} {target1}")
    source2 = "kilogram"
    target2 = "pound"
    result2 = convert_quantity(conversion_data, input_quantity, source2, target2)
    print(f"{input_quantity} {source2} is equal to {result2} {target2}")
    source3 = "liter"
    target3 = "gallon_us"
    result3 = convert_quantity(conversion_data, input_quantity, source3, target3)
    print(f"{input_quantity} {source3} is equal to {result3} {target3}")
    source4 = "meter"
    target4 = "kilogram"
    result4 = convert_quantity(conversion_data, input_quantity, source4, target4)
    print(f"{input_quantity} {source4} is equal to {result4} {target4} (No direct conversion found)")