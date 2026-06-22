VOLUME_CONVERSIONS = {
    'milliliters_to_fluid_ounces': 0.033814,
}

def convert_volume(volume, conversion_key):
    if conversion_key not in VOLUME_CONVERSIONS:
        raise ValueError("Unsupported conversion key")
    return volume * VOLUME_CONVERSIONS[conversion_key]

if __name__ == '__main__':
    sample_value = 250
    result = convert_volume(sample_value, 'milliliters_to_fluid_ounces')
    print(result)