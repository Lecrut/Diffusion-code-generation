VOLUME_CONVERSIONS = {
    'milliliters_to_fluid_ounces': 0.033814,
    'fluid_ounces_to_milliliters': 29.5735
}

def convert_volume(volume, conversion_key):
    if conversion_key not in VOLUME_CONVERSIONS:
        raise ValueError("Unsupported conversion key")
    return volume * VOLUME_CONVERSIONS[conversion_key]

if __name__ == '__main__':
    sample_milliliters = 1500
    result_fluid_ounces = convert_volume(sample_milliliters, 'milliliters_to_fluid_ounces')
    print(f"{sample_milliliters} milliliters is {result_fluid_ounces} fluid ounces")