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
    while current_unit != target_unit:
        if current_unit == "meter":
            if target_unit in ["kilometer", "centimeter", "millimeter"]:
                current_value = convert_units(current_value, "meter", target_unit)
                current_unit = target_unit
            elif target_unit in ["inch", "foot", "mile"]:
                if target_unit == "inch":
                    current_value = convert_units(current_value, "meter", "inch")
                    current_unit = "inch"
                elif target_unit == "foot":
                    current_value = convert_units(current_value, "meter", "foot")
                    current_unit = "foot"
                elif target_unit == "mile":
                    current_value = convert_units(current_value, "meter", "mile")
                    current_unit = "mile"
            else:
                raise ValueError("Invalid target unit for meter chain.")
        elif current_unit == "kilogram":
            if target_unit in ["gram", "pound", "ounce"]:
                current_value = convert_units(current_value, "kilogram", target_unit)
                current_unit = target_unit
            else:
                raise ValueError("Invalid target unit for kilogram chain.")
        elif current_unit == "liter":
            if target_unit == "milliliter":
                current_value = convert_units(current_value, "liter", "milliliter")
                current_unit = "milliliter"
            else:
                raise ValueError("Invalid target unit for liter chain.")
        elif current_unit == "inch":
            if target_unit in ["centimeter", "meter"]:
                current_value = convert_units(current_value, "inch", target_unit)
                current_unit = target_unit
            else:
                raise ValueError("Invalid target unit for inch chain.")
        elif current_unit == "foot":
            if target_unit in ["meter", "inch"]:
                current_value = convert_units(current_value, "foot", target_unit)
                current_unit = target_unit
            else:
                raise ValueError("Invalid target unit for foot chain.")
        elif current_unit == "mile":
            if target_unit in ["kilometer", "meter"]:
                current_value = convert_units(current_value, "mile", "meter")
                current_unit = "meter"
            else:
                raise ValueError("Invalid target unit for mile chain.")
        else:
            raise ValueError(f"Starting unit {current_unit} not supported for chaining.")
    return current_value
if __name__ == '__main__':
    print("--- Test Case 1: Metric to Imperial Chain (Meter to Inch) ---")
    initial_val = 10.0
    from_u = "meter"
    to_u = "inch"
    try:
        result = chained_conversion(initial_val, from_u, to_u)
        print(f"{initial_val} {from_u} is equal to {result} {to_u}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Test Case 2: Imperial to Metric Chain (Mile to Kilometer) ---")
    initial_val = 1.0
    from_u = "mile"
    to_u = "kilometer"
    try:
        result = chained_conversion(initial_val, from_u, to_u)
        print(f"{initial_val} {from_u} is equal to {result} {to_u}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Test Case 3: Metric Sub-unit Conversion (Meter to Millimeter) ---")
    initial_val = 5.0
    from_u = "meter"
    to_u = "millimeter"
    try:
        result = chained_conversion(initial_val, from_u, to_u)
        print(f"{initial_val} {from_u} is equal to {result} {to_u}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Test Case 4: Mass Conversion (Kilogram to Pound) ---")
    initial_val = 2.5
    from_u = "kilogram"
    to_u = "pound"
    try:
        result = chained_conversion(initial_val, from_u, to_u)
        print(f"{initial_val} {from_u} is equal to {result} {to_u}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Test Case 5: Direct Conversion (Foot to Meter) ---")
    initial_val = 6.0
    from_u = "foot"
    to_u = "meter"
    try:
        result = chained_conversion(initial_val, from_u, to_u)
        print(f"{initial_val} {from_u} is equal to {result} {to_u}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Test Case 6: Error Handling (Unsupported Conversion) ---")
    try:
        chained_conversion(10, "meter", "furlong")
    except ValueError as e:
        print(f"Caught expected error: {e}")