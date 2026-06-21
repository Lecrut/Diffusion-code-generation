CONVERSION_FACTORS = {
    'liters_to_milliliters': 1000,
}

def convert_volume(volume, conversion_type):
    if conversion_type not in CONVERSION_FACTORS:
        raise ValueError(f"Unsupported conversion type: {conversion_type}")
    return volume * CONVERSION_FACTORS[conversion_type]

if __name__ == '__main__':
    sample_liters = 3.2
    milliliters = convert_volume(sample_liters, 'liters_to_milliliters')
    print(milliliters)