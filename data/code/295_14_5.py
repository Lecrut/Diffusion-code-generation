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
        raise ValueError("Invalid unit specified")
    if from_unit == to_unit:
        return value
    base_value = value * multipliers[from_unit]
    result = base_value / multipliers[to_unit]
    return result
if __name__ == '__main__':
    unit_multipliers = create_unit_system()
    value = 10
    from_u = 'meter'
    to_u = 'pound'
    try:
        result = convert_units(value, from_u, to_u, unit_multipliers)
        print(f"{value} {from_u} is equal to {result} {to_u}")
        value2 = 5
        from_u2 = 'liter'
        to_u2 = 'gallon'
        result2 = convert_units(value2, from_u2, to_u2, unit_multipliers)
        print(f"{value2} {from_u2} is equal to {result2} {to_u2}")
    except ValueError as e:
        print(f"Error: {e}")