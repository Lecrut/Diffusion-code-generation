def setup_units():
    multipliers = {
        'meter': 1.0,
        'pound': 0.453592,
        'liter': 0.264172,
        'second': 1.0,
        'kilogram': 0.001,
    }
    return multipliers
def convert(value, from_unit, to_unit, multipliers):
    if from_unit not in multipliers or to_unit not in multipliers:
        raise ValueError("Invalid unit specified")
    if from_unit == to_unit:
        return value
    base_value = value * multipliers[from_unit]
    result = base_value / multipliers[to_unit]
    return result
if __name__ == '__main__':
    unit_multipliers = setup_units()
    value = 10
    from_u = 'meter'
    to_u = 'pound'
    try:
        result = convert(value, from_u, to_u, unit_multipliers)
        print(f"{value} {from_u} is equal to {result} {to_u}")
    except ValueError as e:
        print(e)
    value2 = 500
    from_u2 = 'liter'
    to_u2 = 'kilogram'
    try:
        result2 = convert(value2, from_u2, to_u2, unit_multipliers)
        print(f"{value2} {from_u2} is equal to {result2} {to_u2}")
    except ValueError as e:
        print(e)