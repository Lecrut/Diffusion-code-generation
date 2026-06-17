UNIT_MULTIPLIERS = {
    'meter': 1.0,
    'foot': 0.3048,
    'pound': 0.453592,
    'liter': 0.264172,
    'gallon': 3.78541,
}
def convert(value, from_unit, to_unit):
    if from_unit not in UNIT_MULTIPLIERS or to_unit not in UNIT_MULTIPLIERS:
        raise ValueError("Invalid unit specified")
    if from_unit == to_unit:
        return value
    base_value = value * UNIT_MULTIPLIERS[from_unit]
    result = base_value / UNIT_MULTIPLIERS[to_unit]
    return result
if __name__ == '__main__':
    print(f"10 meter to foot: {convert(10, 'meter', 'foot')}")
    print(f"5 pound to liter: {convert(5, 'pound', 'liter')}")
    print(f"2 gallon to liter: {convert(2, 'gallon', 'liter')}")
    print(f"1 meter to meter: {convert(1, 'meter', 'meter')}")