def setup_units():
    multipliers = {
        'meter': 1.0,
        'foot': 0.3048,
        'pound': 0.453592,
        'liter': 0.001,
        'gallon': 3.78541,
        'kilogram': 0.001,
        'millimeter': 0.001,
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
    print(f"--- Testing Conversions ---")
    try:
        result1 = convert(test_value, 'meter', 'foot', unit_multipliers)
        print(f"{test_value} meters is approximately {result1:.4f} feet")
    except ValueError as e:
        print(e)
    try:
        result2 = convert(test_value, 'pound', 'kilogram', unit_multipliers)
        print(f"{test_value} pounds is approximately {result2:.4f} kilograms")
    except ValueError as e:
        print(e)
    try:
        result3 = convert(test_value, 'liter', 'gallon', unit_multipliers)
        print(f"{test_value} liters is approximately {result3:.4f} gallons")
    except ValueError as e:
        print(e)
    try:
        result4 = convert(5, 'meter', 'meter', unit_multipliers)
        print(f"5 meters is {result4} meters")
    except ValueError as e:
        print(e)