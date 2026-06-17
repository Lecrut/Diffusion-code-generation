import sys
def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        ('meter', 'foot'): 3.28084,
        ('foot', 'meter'): 0.3048,
        ('kilogram', 'pound'): 2.20462,
        ('pound', 'kilogram'): 0.453592,
    }
    key = (from_unit, to_unit)
    if key in conversion_factors:
        return value * conversion_factors[key]
    else:
        return None
if __name__ == '__main__':
    initial_value = 10
    from_unit = 'meter'
    to_unit = 'foot'
    result = convert_units(initial_value, from_unit, to_unit)
    if result is not None:
        print(f"Initial Value: {initial_value} {from_unit}")
        print(f"Conversion Pair: {from_unit} to {to_unit}")
        print(f"Result: {result:.4f} {to_unit}")
    else:
        print("Error: Conversion pair not supported.")