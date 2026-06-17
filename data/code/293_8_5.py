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
        elif to_unit == "gallon":
            return value * 3.785411784
    elif from_unit == "inch":
        if to_unit == "centimeter":
            return value * 2.54
        elif to_unit == "meter":
            return value / 39.3701
    elif from_unit == "foot":
        if to_unit == "meter":
            return value * 0.3048
        elif to_unit == "inch":
            return value * 12.0
    elif from_unit == "mile":
        if to_unit == "kilometer":
            return value * 1.609344
        elif to_unit == "mile":
            return value
        elif to_unit == "foot":
            return value * 5280.0
    raise ValueError(f"Unsupported conversion: {from_unit} to {to_unit}")
def chained_conversion(initial_value, start_unit, end_unit):
    if start_unit == end_unit:
        return initial_value
    current_value = initial_value
    current_unit = start_unit
    conversion_map = {
        ("meter", "kilometer"): lambda v: v / 1000.0,
        ("kilometer", "meter"): lambda v: v * 1000.0,
        ("meter", "centimeter"): lambda v: v * 100.0,
        ("centimeter", "meter"): lambda v: v / 100.0,
        ("inch", "centimeter"): lambda v: v * 2.54,
        ("centimeter", "inch"): lambda v: v / 2.54,
        ("foot", "meter"): lambda v: v * 0.3048,
        ("meter", "foot"): lambda v: v / 0.3048,
        ("mile", "kilometer"): lambda v: v * 1.609344,
        ("kilometer", "mile"): lambda v: v / 1.609344,
        ("foot", "inch"): lambda v: v * 12.0,
    }
    def recursive_convert(value, current, target):
        if current == target:
            return value
        for next_unit in ["kilometer", "centimeter", "millimeter", "gram", "pound", "ounce", "gallon", "meter", "inch", "foot", "mile"]:
            if next_unit != current:
                try:
                    converted_value = convert_units(value, current, next_unit)
                    result = recursive_convert(converted_value, next_unit, target)
                    if result is not None:
                        return result
                except ValueError:
                    continue
        return None
    path = [start_unit]
    while path[-1] != end_unit:
        current = path[-1]
        found_next = False
        for next_unit in ["kilometer", "centimeter", "millimeter", "gram", "pound", "ounce", "gallon", "meter", "inch", "foot", "mile"]:
            if next_unit != current:
                try:
                    new_value = convert_units(current_value, current, next_unit)
                    path.append(next_unit)
                    current_value = new_value
                    found_next = True
                    break
                except ValueError:
                    continue
        if not found_next:
            return None
    return current_value if path[-1] == end_unit else None
if __name__ == '__main__':
    initial_length = 10.0
    start = "meter"
    end = "foot"
    result1 = chained_conversion(initial_length, start, end)
    print(f"Chained Conversion: {initial_length} {start} to {end}")
    if result1 is not None:
        print(f"Result: {result1:.4f} {end}\n")
    else:
        print("Conversion failed for Sample 1\n")
    initial_mass = 500.0
    start = "kilogram"
    end = "gram"
    result2 = chained_conversion(initial_mass, start, end)
    print(f"Chained Conversion: {initial_mass} {start} to {end}")
    if result2 is not None:
        print(f"Result: {result2:.2f} {end}\n")
    else:
        print("Conversion failed for Sample 2\n")
    initial_distance = 100.0
    start = "mile"
    end = "kilometer"
    result3 = chained_conversion(initial_distance, start, end)
    print(f"Chained Conversion: {initial_distance} {start} to {end}")
    if result3 is not None:
        print(f"Result: {result3:.4f} {end}\n")
    else:
        print("Conversion failed for Sample 3\n")
    initial_inch = 12.0
    start = "inch"
    end = "meter"
    result4 = chained_conversion(initial_inch, start, end)
    print(f"Chained Conversion: {initial_inch} {start} to {end}")
    if result4 is not None:
        print(f"Result: {result4:.4f} {end}\n")
    else:
        print("Conversion failed for Sample 4\n")