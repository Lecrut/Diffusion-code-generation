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
        raise ValueError("Invalid unit specified")
    if from_unit == to_unit:
        return value
    base_value = value * multipliers[from_unit]
    result = base_value / multipliers[to_unit]
    return result
if __name__ == '__main__':
    unit_multipliers = create_unit_system()
    print("Unit Multipliers:")
    for unit, multiplier in unit_multipliers.items():
        print(f"{unit}: {multiplier}")
    value = 10
    from_u = 'meter'
    to_u = 'foot'
    try:
        converted_value = convert_units(value, from_u, to_u, unit_multipliers)
        print(f"\nConverting {value} {from_u} to {to_u}: {converted_value}")
        value = 100
        from_u = 'pound'
        to_u = 'kilogram'
        converted_value = convert_units(value, from_u, to_u, unit_multipliers)
        print(f"Converting {value} {from_u} to {to_u}: {converted_value}")
    except ValueError as e:
        print(f"Error: {e}")