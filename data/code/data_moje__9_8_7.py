import numpy as np

CONVERSION_FACTORS = {
    'liters': 1.0,
    'milliliters': 0.001,
    'gallons': 3.78541,
    'quarts': 0.946353,
    'pints': 0.473176,
    'cups': 0.24,
    'cubic_meters': 1000.0,
    'cubic_inches': 0.0163871,
}

def convert_volumes(values, from_unit, to_unit):
    factor_from = CONVERSION_FACTORS.get(from_unit)
    factor_to = CONVERSION_FACTORS.get(to_unit)
    if factor_from is None or factor_to is None:
        raise ValueError(f"Unsupported unit: {from_unit} or {to_unit}")
    base_values = np.asarray(values, dtype=float) / factor_from
    result = base_values * factor_to
    return result

if __name__ == '__main__':
    sample_values = np.array([1.0, 2.5, 10.0, 0.5])
    result_liters_to_gallons = convert_volumes(sample_values, 'liters', 'gallons')
    print(result_liters_to_gallons)