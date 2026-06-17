def create_unit_system():
    multipliers = {
        'meter': 1.0,
        'pound': 0.453592,
        'liter': 0.264172,
        'second': 1.0,
        'kilogram': 0.001,
        'gallon': 3.78541,
    }
    return multipliers
def convert_units(value, from_unit, to_unit, multipliers):
    if from_unit not in multipliers or to_unit not in multipliers:
        raise ValueError("One or both units are not defined in the system.")
    if from_unit == to_unit:
        return value
    value_in_base = value * multipliers[from_unit]
    result = value_in_base / multipliers[to_unit]
    return result
if __name__ == '__main__':
    unit_multipliers = create_unit_system()
    print("Unit Multipliers:")
    for unit, multiplier in unit_multipliers.items():
        print(f"{unit}: {multiplier}")
    try:
        value = 10
        from_unit = 'meter'
        to_unit = 'pound'
        result = convert_units(value, from_unit, to_unit, unit_multipliers)
        print(f"\nConversion: {value} {from_unit} is approximately {result:.4f} {to_unit}")
        value = 5
        from_unit = 'liter'
        to_unit = 'gallon'
        result = convert_units(value, from_unit, to_unit, unit_multipliers)
        print(f"Conversion: {value} {from_unit} is approximately {result:.4f} {to_unit}")
    except ValueError as e:
        print(f"\nError during conversion: {e}")