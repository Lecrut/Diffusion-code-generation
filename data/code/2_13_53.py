VOLUME_CONVERSION = {
    'milliliters': 0.033814,
}

def convert_volume(volume, from_unit):
    if from_unit not in VOLUME_CONVERSION:
        raise ValueError(f"Unsupported volume unit: {from_unit}")
    conversion_factor = VOLUME_CONVERSION[from_unit]
    return volume * conversion_factor

if __name__ == '__main__':
    sample_milliliters = 250
    try:
        result = convert_volume(sample_milliliters, 'milliliters')
        print(result)
    except ValueError as e:
        print(e)