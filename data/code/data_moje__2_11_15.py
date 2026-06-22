CONVERSION_FACTORS = {
    'm3': 1.0,
    'cm3': 1e-6,
    'liter': 0.001,
    'ml': 1e-6,
    'gallon': 0.00378541,
    'quart': 0.000946353,
    'pint': 0.000473176,
    'cup': 0.000236588,
}

def standardize_volume(volumes, source_unit='liter'):
    if source_unit not in CONVERSION_FACTORS:
        raise ValueError(f"Unknown unit: {source_unit}")
    factor = CONVERSION_FACTORS[source_unit]
    return {key: value * factor for key, value in volumes.items()}

if __name__ == '__main__':
    data = {'water': 10.0, 'sand': 5.5}
    result = standardize_volume(data, 'liter')
    print(result)