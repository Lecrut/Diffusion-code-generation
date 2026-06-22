def convert_to_kg(weights):
    units_to_kg = {'kg': 1.0, 'g': 0.001, 'mg': 1e-06, 'lb': 0.453592, 'oz': 0.0283495, 'st': 6.35029}
    result = []
    for value, unit in weights:
        unit_lower = unit.lower()
        if unit_lower in units_to_kg:
            kg_value = value * units_to_kg[unit_lower]
            result.append(kg_value)
        else:
            raise ValueError(f'Unknown unit: {unit}')
    return result
if __name__ == '__main__':
    sample_weights = [(1000, 'g'), (5, 'kg'), (10, 'lb'), (16, 'oz'), (1, 'mg')]
    converted_weights = convert_to_kg(sample_weights)
    print(converted_weights)