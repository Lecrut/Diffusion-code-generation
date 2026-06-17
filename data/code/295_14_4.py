def create_unit_system():
    multipliers = {
        'meter': 1.0,
        'foot': 0.3048,
        'inch': 0.0254,
        'pound': 0.453592,
        'kilogram': 0.001,
        'liter': 0.001,
        'gallon': 3.78541,
    }
    return multipliers
def convert_units(value, from_unit, to_unit, multipliers):
    if from_unit not in multipliers or to_unit not in multipliers:
        raise ValueError("Invalid unit specified.")
    if from_unit == to_unit:
        return value
    base_value = value * multipliers[from_unit]
    result = base_value / multipliers[to_unit]
    return result
if __name__ == '__main__':
    unit_multipliers = create_unit_system()
    test_value = 10
    print(f"Base Multipliers: {unit_multipliers}")
    print("-" * 30)
    try:
        result1 = convert_units(test_value, 'meter', 'foot', unit_multipliers)
        print(f"{test_value} meters is equal to {result1:.4f} feet")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result2 = convert_units(5, 'pound', 'kilogram', unit_multipliers)
        print(f"5 pounds is equal to {result2:.4f} kilograms")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result3 = convert_units(10, 'liter', 'gallon', unit_multipliers)
        print(f"10 liters is equal to {result3:.4f} gallons")
    except ValueError as e:
        print(f"Error: {e}")