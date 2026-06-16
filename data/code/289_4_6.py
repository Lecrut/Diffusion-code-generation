def convert_distance(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise TypeError("Input value must be numeric.")
    if from_unit == to_unit:
        return float(value)
    conversion_factors = {
        ('m', 'km'): 1000.0,
        ('km', 'm'): 1.0 / 1000.0,
        ('mi', 'km'): 1.609344,
        ('km', 'mi'): 1.0 / 1.609344,
        ('ft', 'm'): 0.3048,
        ('m', 'ft'): 1.0 / 0.3048,
    }
    unit_pair = (from_unit.lower(), to_unit.lower())
    if unit_pair in conversion_factors:
        return float(value) * conversion_factors[unit_pair]
    else:
        raise ValueError(f"Unsupported unit conversion: {from_unit} to {to_unit}")
if __name__ == '__main__':
    test_cases = [
        (10, 'm', 'km'),
        (5, 'km', 'm'),
        (100, 'mi', 'km'),
        (2.5, 'ft', 'm'),
        (10, 'm', 'm'),
        (1, 'km', 'mi'),
    ]
    for value, from_unit, to_unit in test_cases:
        try:
            result = convert_distance(value, from_unit, to_unit)
            print(f"{value} {from_unit} is equal to {result:.6f} {to_unit}")
        except (TypeError, ValueError) as e:
            print(f"Error processing {value} {from_unit} to {to_unit}: {e}")