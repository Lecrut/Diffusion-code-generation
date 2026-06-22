UNIT_TO_CUBIC_METER = {
    'liter': 0.001,
    'milliliter': 0.000001,
    'gallon': 0.00378541,
    'cubic_foot': 0.0283168,
    'cubic_inch': 0.0000163871,
    'barrel': 0.158987,
}

def standardize_volume(measurements):
    standardized = {}
    for key, val in measurements.items():
        unit = key.lower()
        factor = UNIT_TO_CUBIC_METER.get(unit, 1.0)
        standardized[key] = val * factor
    return standardized

if __name__ == '__main__':
    test_data = {
        'liter': 100.0,
        'gallon': 5.0,
        'cubic_foot': 2.0,
        'milliliter': 500.0,
    }
    result = standardize_volume(test_data)
    print(result)