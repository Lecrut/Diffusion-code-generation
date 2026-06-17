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
    raise ValueError(f"Unsupported conversion: {from_unit} to {to_unit}")
def chained_conversion(initial_value, start_unit, end_unit):
    current_value = initial_value
    current_unit = start_unit
    if start_unit == end_unit:
        return current_value
    conversion_steps = []
    possible_conversions = {
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
    }
    queue = [(current_unit, current_value)]
    visited = {current_unit: current_value}
    while queue:
        u, v = queue.pop(0)
        if u == end_unit:
            return v
        for (from_u, to_u), func in possible_conversions.items():
            if from_u == u:
                new_v = func(v)
                if to_u == end_unit:
                    return new_v
                if to_u not in visited or new_v < visited[to_u] if to_u in visited else True:
                    visited[to_u] = new_v
                    queue.append((to_u, new_v))
    raise ValueError(f"No conversion path found between {start_unit} and {end_unit}")
if __name__ == '__main__':
    print("--- Test Case 1: Metric Chain (Meter to Kilometer) ---")
    try:
        result1 = chained_conversion(1000, "meter", "kilometer")
        print(f"1000 meters to kilometers: {result1}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Test Case 2: Metric Chain (Centimeter to Meter) ---")
    try:
        result2 = chained_conversion(500, "centimeter", "meter")
        print(f"500 centimeters to meters: {result2}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Test Case 3: Imperial Chain (Foot to Meter) ---")
    try:
        result3 = chained_conversion(10, "foot", "meter")
        print(f"10 feet to meters: {result3}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Test Case 4: Mixed Chain (Mile to Kilometer) ---")
    try:
        result4 = chained_conversion(2, "mile", "kilometer")
        print(f"2 miles to kilometers: {result4}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Test Case 5: Direct Conversion (Kilogram to Pound) ---")
    try:
        result5 = chained_conversion(10, "kilogram", "pound")
        print(f"10 kilograms to pounds: {result5}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Test Case 6: Invalid Conversion ---")
    try:
        chained_conversion(10, "meter", "furlong")
    except ValueError as e:
        print(f"Caught expected error: {e}")