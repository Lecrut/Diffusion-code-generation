conversion_factors = {
    'water': 1.0,
    'sand': 0.8,
    'oil': 0.9,
    'air': 0.0012
}

def standardize_volume(volumes):
    standardized = {}
    for substance, value in volumes.items():
        if substance in conversion_factors:
            standardized[substance] = value * conversion_factors[substance]
        else:
            raise ValueError(f"Unknown substance: {substance}")
    return standardized

if __name__ == '__main__':
    sample_volumes = {
        'water': 10.0,
        'sand': 5.5,
        'oil': 7.2
    }
    result = standardize_volume(sample_volumes)
    print(result)