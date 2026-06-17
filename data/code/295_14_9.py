def setup_units():
    multipliers = {
        'meter': 1.0,
        'foot': 0.3048,
        'pound': 0.453592,
        'liter': 0.264172,
        'gallon': 3.78541,
        'kilogram': 0.001,
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
    print(f"Base unit: meter")
    print(f"{test_value} meters to feet: {convert(test_value, 'meter', 'foot', unit_multipliers)}")
    print(f"{test_value} pounds to kilograms: {convert(test_value, 'pound', 'kilogram', unit_multipliers)}")
    print(f"{test_value} liters to gallons: {convert(test_value, 'liter', 'gallon', unit_multipliers)}")