import numpy as np
CONVERSION_FACTORS = {'cubic_meters_to_liters': 1000.0, 'liters_to_cubic_meters': 0.001, 'cubic_feet_to_liters': 28.316846592, 'liters_to_cubic_feet': 1.0 / 28.316846592, 'gallons_to_liters': 3.785411784, 'liters_to_gallons': 1.0 / 3.785411784, 'cubic_inches_to_liters': 0.016387064, 'liters_to_cubic_inches': 1.0 / 0.016387064}

def convert_volumes(volumes, unit_from, unit_to):
    if unit_from == unit_to:
        return volumes.copy()
    factors = CONVERSION_FACTORS
    if (unit_from, unit_to) in factors:
        factor = factors[unit_from, unit_to]
    else:
        inv_key = (unit_to, unit_from)
        if inv_key in factors:
            factor = 1.0 / factors[inv_key]
        else:
            raise ValueError(f'Unsupported conversion from {unit_from} to {unit_to}')
    result = volumes * factor
    return result
if __name__ == '__main__':
    volumes = np.array([1.0, 2.5, 10.0, 100.0])
    converted = convert_volumes(volumes, 'cubic_meters', 'liters')
    print(converted)