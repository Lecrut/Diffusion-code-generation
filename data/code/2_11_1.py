def standardize_volume(measurements: dict, base_unit: str = 'm3') -> dict:
    CONVERSION_TO_BASE = {
        'm3': {'m3': 1.0, 'cm3': 1e-6, 'liter': 1e-3, 'ml': 1e-6, 'gallon': 0.00378541},
        'cm3': {'m3': 1000000.0, 'cm3': 1.0, 'liter': 1000.0, 'ml': 1000.0, 'gallon': 3785.41},
        'liter': {'m3': 1000.0, 'cm3': 1000.0, 'liter': 1.0, 'ml': 1000.0, 'gallon': 0.264172},
        'ml': {'m3': 1000000.0, 'cm3': 1000000.0, 'liter': 1000.0, 'ml': 1.0, 'gallon': 264.172},
        'gallon': {'m3': 264.172, 'cm3': 378541.0, 'liter': 3.78541, 'ml': 3785.41, 'gallon': 1.0}
    }

    if base_unit not in CONVERSION_TO_BASE:
        raise ValueError(f"Base unit '{base_unit}' is not supported.")

    factors = CONVERSION_TO_BASE[base_unit]
    result = {}

    for name, value in measurements.items():
        if not isinstance(value, (int, float)):
            raise TypeError(f"Value for '{name}' must be numeric.")
        
        unit = 'm3'
        if isinstance(name, tuple) and len(name) == 2:
            unit = name[1]
        else:
            unit = name.lower()
            if unit not in factors:
                raise ValueError(f"Unit '{unit}' is not supported for standardization to '{base_unit}'.")
        
        result[name] = value * factors[unit]

    return result

if __name__ == '__main__':
    samples = {
        'water_m3': 10.0,
        'sand_cm3': 5.5,
        'oil_liter': 5.0
    }
    result = standardize_volume(samples, 'm3')
    print(result)