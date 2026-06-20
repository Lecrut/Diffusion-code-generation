def convert_to_kilograms(measurements: list) -> list:
    conversion_factors = {'kg': 1.0, 'g': 0.001, 'mg': 1e-06, 'lb': 0.45359237, 'oz': 0.028349523125, 'ton': 907.18474, 't': 907.18474}
    results = []
    for item in measurements:
        if not isinstance(item, (list, tuple)):
            raise TypeError(f'Expected a tuple or list for each measurement, got {type(item)}')
        if len(item) != 2:
            raise ValueError(f'Each measurement must contain exactly two elements (value and unit). Got: {item}')
        value, unit = item
        unit_lower = unit.lower()
        if unit_lower not in conversion_factors:
            raise ValueError(f"Unknown weight unit: '{unit}'")
        try:
            numeric_value = float(value)
        except (ValueError, TypeError):
            raise ValueError(f"Invalid numeric value for weight: '{value}'")
        kg_value = numeric_value * conversion_factors[unit_lower]
        results.append(kg_value)
    return results
if __name__ == '__main__':
    sample_weights = [(100, 'kg'), (500, 'g'), (1.5, 'lb'), (2000, 'mg'), (0.5, 'oz')]
    converted_weights = convert_to_kilograms(sample_weights)
    print(converted_weights)