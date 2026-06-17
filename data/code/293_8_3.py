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
    raise ValueError(f"Unsupported conversion: {from_unit} to {to_unit}")
def chained_conversion(initial_value, initial_unit, target_unit):
    current_value = initial_value
    current_unit = initial_unit
    conversion_steps = []
    while current_unit != target_unit:
        found_conversion = False
        if current_unit == "meter":
            if target_unit in ["kilometer", "centimeter", "millimeter"]:
                new_value = convert_units(current_value, "meter", target_unit)
                current_value = new_value
                current_unit = target_unit
                conversion_steps.append((current_unit, current_value))
                found_conversion = True
        elif current_unit == "kilogram":
            if target_unit in ["gram", "pound", "ounce"]:
                new_value = convert_units(current_value, "kilogram", target_unit)
                current_value = new_value
                current_unit = target_unit
                conversion_steps.append((current_unit, current_value))
                found_conversion = True
        elif current_unit == "liter":
            if target_unit == "milliliter":
                new_value = convert_units(current_value, "liter", "milliliter")
                current_value = new_value
                current_unit = target_unit
                conversion_steps.append((current_unit, current_value))
                found_conversion = True
        elif current_unit == "inch":
            if target_unit in ["centimeter", "meter"]:
                new_value = convert_units(current_value, "inch", target_unit)
                current_value = new_value
                current_unit = target_unit
                conversion_steps.append((current_unit, current_value))
                found_conversion = True
        elif current_unit == "foot":
            if target_unit in ["meter", "inch"]:
                new_value = convert_units(current_value, "foot", target_unit)
                current_value = new_value
                current_unit = target_unit
                conversion_steps.append((current_unit, current_value))
                found_conversion = True
        elif current_unit == target_unit:
            break
        if not found_conversion and current_unit != target_unit:
            raise ValueError(f"No direct conversion path found from {current_unit} to {target_unit}")
    return current_value, conversion_steps
if __name__ == '__main__':
    print("--- Test Case 1: Metric to Imperial (Length) ---")
    initial_val = 10.0
    initial_unit = "meter"
    target_unit = "foot"
    try:
        result, steps = chained_conversion(initial_val, initial_unit, target_unit)
        print(f"Initial: {initial_val} {initial_unit}")
        print(f"Target: {result} {target_unit}")
        print("Steps taken:")
        for step in steps:
            print(f"  Converted to {step[0]}: {step[1]}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Test Case 2: Mass Conversion ---")
    initial_val = 5.0
    initial_unit = "kilogram"
    target_unit = "ounce"
    try:
        result, steps = chained_conversion(initial_val, initial_unit, target_unit)
        print(f"Initial: {initial_val} {initial_unit}")
        print(f"Target: {result} {target_unit}")
        print("Steps taken:")
        for step in steps:
            print(f"  Converted to {step[0]}: {step[1]}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Test Case 3: Complex Chain (Inch to Meter) ---")
    initial_val = 30.48
    initial_unit = "inch"
    target_unit = "meter"
    try:
        result, steps = chained_conversion(initial_val, initial_unit, target_unit)
        print(f"Initial: {initial_val} {initial_unit}")
        print(f"Target: {result} {target_unit}")
        print("Steps taken:")
        for step in steps:
            print(f"  Converted to {step[0]}: {step[1]}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Test Case 4: Same Unit Conversion ---")
    initial_val = 100.0
    initial_unit = "meter"
    target_unit = "meter"
    try:
        result, steps = chained_conversion(initial_val, initial_unit, target_unit)
        print(f"Initial: {initial_val} {initial_unit}")
        print(f"Target: {result} {target_unit}")
        print("Steps taken:")
        if not steps:
            print("No conversions needed.")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Test Case 5: Unsupported Conversion ---")
    initial_val = 10.0
    initial_unit = "meter"
    target_unit = "furlong"
    try:
        chained_conversion(initial_val, initial_unit, target_unit)
    except ValueError as e:
        print(f"Caught expected error: {e}")