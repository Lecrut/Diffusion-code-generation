def setup_units():
    multipliers = {
        'meter': 1.0,
        'foot': 0.3048,
        'inch': 0.0254,
        'pound': 0.453592,
        'kilogram': 0.001,
        'liter': 0.001,
        'gallon_us': 3.78541,
    }
    return multipliers
def convert(value, from_unit, to_unit, multipliers):
    if from_unit not in multipliers or to_unit not in multipliers:
        raise ValueError("Invalid unit specified")
    base_value = value * multipliers[from_unit]
    result = base_value / multipliers[to_unit]
    return result
if __name__ == '__main__':
    unit_multipliers = setup_units()
    test_value = 10
    print(f"--- Conversion Tests (Starting with {test_value} of meter) ---")
    try:
        result1 = convert(test_value, 'meter', 'foot', unit_multipliers)
        print(f"{test_value} meter is equal to {result1:.4f} foot")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result2 = convert(5, 'pound', 'kilogram', unit_multipliers)
        print(f"5 pound is equal to {result2:.4f} kilogram")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result3 = convert(10, 'liter', 'gallon_us', unit_multipliers)
        print(f"10 liter is equal to {result3:.4f} gallon_us")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result4 = convert(20, 'meter', 'meter', unit_multipliers)
        print(f"20 meter is equal to {result4:.4f} meter")
    except ValueError as e:
        print(f"Error: {e}")