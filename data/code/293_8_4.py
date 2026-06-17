import math
def convert_units(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "meter":
        if to_unit == "kilometer":
            return value / 1000.0
        elif to_unit == "centimeter":
            return value * 100.0
        elif to_unit == "millimeter":
            return value * 1000.0
    elif from_unit == "kilogram":
        if to_unit == "gram":
            return value * 1000.0
        elif to_unit == "pound":
            return value * 2.2046226218
        elif to_unit == "ounce":
            return value * 35.27396195
    elif from_unit == "liter":
        if to_unit == "milliliter":
            return value * 1000.0
    elif from_unit == "inch":
        if to_unit == "centimeter":
            return value * 2.54
        elif to_unit == "meter":
            return value * 0.0254
    elif from_unit == "foot":
        if to_unit == "meter":
            return value * 0.3048
        elif to_unit == "inch":
            return value * 12.0
    elif from_unit == "mile":
        if to_unit == "kilometer":
            return value * 1.609344
        elif to_unit == "meter":
            return value * 1609.344
        elif to_unit == "mile":
            return value
    else:
        raise ValueError(f"Unknown unit: {from_unit}")
def chained_conversion(initial_value, initial_unit, target_unit):
    current_value = initial_value
    current_unit = initial_unit
    if current_unit == target_unit:
        return current_value
    while current_unit != target_unit:
        try:
            converted_value = convert_units(current_value, current_unit, target_unit)
            current_value = converted_value
            current_unit = target_unit
        except ValueError as e:
            return f"Error during conversion: {e}"
    return current_value
if __name__ == '__main__':
    print("--- Test Case 1: Metric to Imperial (Length) ---")
    initial_length = 10.0
    initial_unit = "meter"
    target_unit = "foot"
    result1 = chained_conversion(initial_length, initial_unit, target_unit)
    print(f"{initial_length} {initial_unit} is equal to {result1} {target_unit}\n")
    print("--- Test Case 2: Imperial to Metric (Mass) ---")
    initial_mass = 150.0
    initial_unit = "pound"
    target_unit = "kilogram"
    result2 = chained_conversion(initial_mass, initial_unit, target_unit)
    print(f"{initial_mass} {initial_unit} is equal to {result2} {target_unit}\n")
    print("--- Test Case 3: Chained Conversion (Complex Path) ---")
    initial_value = 100.0
    initial_unit = "mile"
    target_unit = "centimeter"
    result3 = chained_conversion(initial_value, initial_unit, target_unit)
    print(f"{initial_value} {initial_unit} is equal to {result3} {target_unit}\n")
    print("--- Test Case 4: Same Unit ---")
    initial_value = 50.0
    initial_unit = "meter"
    target_unit = "meter"
    result4 = chained_conversion(initial_value, initial_unit, target_unit)
    print(f"{initial_value} {initial_unit} is equal to {result4} {target_unit}\n")
    print("--- Test Case 5: Metric Sub-conversion ---")
    initial_value = 2.5
    initial_unit = "kilometer"
    target_unit = "millimeter"
    result5 = chained_conversion(initial_value, initial_unit, target_unit)
    print(f"{initial_value} {initial_unit} is equal to {result5} {target_unit}\n")