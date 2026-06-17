def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        ('meter', 'foot'): 3.28084,
        ('foot', 'meter'): 0.3048,
        ('kilogram', 'gram'): 1000,
        ('gram', 'kilogram'): 0.001
    }
    key = (from_unit, to_unit)
    if key in conversion_factors:
        result = value * conversion_factors[key]
        return result
    else:
        return "Conversion not supported for this pair."
if __name__ == '__main__':
    initial_value = 10
    from_unit = 'meter'
    to_unit = 'foot'
    result = convert_units(initial_value, from_unit, to_unit)
    print(f"Initial Value: {initial_value}")
    print(f"Conversion Pair: {from_unit} to {to_unit}")
    print(f"Result: {result}")