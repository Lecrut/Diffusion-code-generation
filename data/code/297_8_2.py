import math
def convert_unit_iterative(value, source_unit, target_unit):
    if source_unit == target_unit:
        return value
    conversion_factors = {}
    base_unit = 1.0
    if source_unit == "m" and target_unit in ["km", "cm"]:
        conversion_factors["m"] = 1.0
        conversion_factors["km"] = 1000.0
        conversion_factors["cm"] = 0.01
    elif source_unit == "s" and target_unit in ["min", "h"]:
        conversion_factors["s"] = 1.0
        conversion_factors["min"] = 60.0
        conversion_factors["h"] = 3600.0
    else:
        if source_unit == "A" and target_unit == "B":
            conversion_factors["A"] = 1.5
            conversion_factors["B"] = 0.6666666666666666      
        else:
            raise ValueError(f"Conversion from {source_unit} to {target_unit} is not defined in this system.")
    value_in_base = value
    if source_unit in conversion_factors and target_unit in conversion_factors:
        intermediate_value = value * conversion_factors[source_unit]
        result = intermediate_value / conversion_factors[target_unit]
        return result
    else:
        if source_unit == "A" and target_unit == "B":
            return value * 1.5 / (2/3)                                                                                                                                       
            return value * conversion_factors[source_unit] / conversion_factors[target_unit]
if __name__ == '__main__':
    value1 = 5000.0
    source1 = "m"
    target1 = "km"
    result1 = convert_unit_iterative(value1, source1, target1)
    print(f"{value1} {source1} is {result1} {target1}")
    value2 = 180.0
    source2 = "s"
    target2 = "min"
    result2 = convert_unit_iterative(value2, source2, target2)
    print(f"{value2} {source2} is {result2} {target2}")
    value3 = 10.0
    source3 = "A"
    target3 = "B"
    result3 = convert_unit_iterative(value3, source3, target3)
    print(f"{value3} {source3} is {result3} {target3}")
    value4 = 123.45
    source4 = "m"
    target4 = "m"
    result4 = convert_unit_iterative(value4, source4, target4)
    print(f"{value4} {source4} is {result4} {target4}")
    try:
        convert_unit_iterative(10, "m", "s")
    except ValueError as e:
        print(f"Error caught successfully: {e}")