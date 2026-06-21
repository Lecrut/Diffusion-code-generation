CONVERSION_TABLE = {
    'milliliters_to_fluid_ounces': 0.033814
}

def convert_volume(volume, conversion_key):
    if conversion_key not in CONVERSION_TABLE:
        raise ValueError("Unsupported conversion key")
    return volume * CONVERSION_TABLE[conversion_key]

if __name__ == '__main__':
    sample_value = 750
    result = convert_volume(sample_value, 'milliliters_to_fluid_ounces')
    print(result)