UNIT_MULTIPLIERS = {
    'meter': 1.0,
    'foot': 0.3048,
    'pound': 0.453592,
    'liter': 0.264172,
    'gallon': 3.78541,
}
def convert(value, from_unit, to_unit):
    if from_unit not in UNIT_MULTIPLIERS or to_unit not in UNIT_MULTIPLIERS:
        raise ValueError("Invalid unit specified.")
    if from_unit == to_unit:
        return value
    if from_unit in ['meter', 'foot']:
        base_unit = 'meter'
    elif from_unit in ['pound']:
        base_unit = 'pound'
    else:
        raise ValueError("Conversion not supported between these units.")
    value_in_base = value * UNIT_MULTIPLIERS[from_unit]
    if to_unit in ['meter', 'foot']:
        return value_in_base / UNIT_MULTIPLIERS[to_unit]
    elif to_unit == 'pound':
        return value_in_base / UNIT_MULTIPLIERS[to_unit]
    else:
        raise ValueError("Unsupported target unit for conversion.")
if __name__ == '__main__':
    sample_value = 10
    from_u = 'meter'
    to_u = 'foot'
    try:
        result = convert(sample_value, from_u, to_u)
        print(f"{sample_value} {from_u} is equal to {result:.4f} {to_u}")
        sample_value_mass = 5
        from_u_mass = 'pound'
        to_u_mass = 'liter'                                                                                                                               
        result_len = convert(10, 'meter', 'foot')
        print(f"10 meter is equal to {result_len:.4f} foot")
    except ValueError as e:
        print(f"Error: {e}")