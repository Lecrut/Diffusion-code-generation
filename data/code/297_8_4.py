import math
def convert_unit_iterative(value, source_unit, target_unit):
    if source_unit == target_unit:
        return value
    conversion_factors = {}
    if source_unit == "meter" and target_unit == "foot":
        conversion_factors["meter_to_foot"] = 3.28084
    elif source_unit == "foot" and target_unit == "meter":
        conversion_factors["foot_to_meter"] = 0.3048
    elif source_unit == "kilogram" and target_unit == "gram":
        conversion_factors["kg_to_g"] = 1000.0
    elif source_unit == "gram" and target_unit == "kilogram":
        conversion_factors["g_to_kg"] = 0.001
    elif source_unit == "liter" and target_unit == "milliliter":
        conversion_factors["liter_to_milliliter"] = 1000.0
    elif source_unit == "milliliter" and target_unit == "liter":
        conversion_factors["milliliter_to_liter"] = 0.001
    else:
        raise ValueError(f"Unsupported unit conversion: {source_unit} to {target_unit}")
    current_value = value
    if source_unit == "meter" or source_unit == "foot":
        if source_unit == "meter":
            base_value = current_value
        else:                        
            base_value = current_value * conversion_factors["foot_to_meter"]
        if target_unit == "meter":
            return base_value
        elif target_unit == "foot":
            return base_value / conversion_factors["meter_to_foot"]
    elif source_unit == "kilogram" or source_unit == "gram":
        if source_unit == "kilogram":
            base_value = current_value
        else:                        
            base_value = current_value / conversion_factors["kg_to_g"]
        if target_unit == "kilogram":
            return base_value
        elif target_unit == "gram":
            return base_value * conversion_factors["kg_to_g"]
    elif source_unit == "liter" or source_unit == "milliliter":
        if source_unit == "liter":
            base_value = current_value
        else:                              
            base_value = current_value / conversion_factors["liter_to_milliliter"]
        if target_unit == "liter":
            return base_value
        elif target_unit == "milliliter":
            return base_value * conversion_factors["liter_to_milliliter"]
    else:
        raise ValueError("Conversion logic failed for defined units.")
if __name__ == '__main__':
    value1 = 10.0
    source1 = "meter"
    target1 = "foot"
    result1 = convert_unit_iterative(value1, source1, target1)
    print(f"{value1} {source1} is equal to {result1} {target1}")
    value2 = 5.5
    source2 = "kilogram"
    target2 = "gram"
    result2 = convert_unit_iterative(value2, source2, target2)
    print(f"{value2} {source2} is equal to {result2} {target2}")
    value3 = 2.5
    source3 = "liter"
    target3 = "milliliter"
    result3 = convert_unit_iterative(value3, source3, target3)
    print(f"{value3} {source3} is equal to {result3} {target3}")
    value4 = 100
    source4 = "meter"
    target4 = "meter"
    result4 = convert_unit_iterative(value4, source4, target4)
    print(f"{value4} {source4} is equal to {result4} {target4}")
    value5 = 100.0
    source5 = "foot"
    target5 = "meter"
    result5 = convert_unit_iterative(value5, source5, target5)
    print(f"{value5} {source5} is equal to {result5} {target5}")