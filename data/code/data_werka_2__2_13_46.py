VOLUME_CONVERSION_FACTOR = 0.033814

def convert_milliliters_to_fluid_ounces(milliliters):
    if milliliters < 0:
        raise ValueError("Volume cannot be negative")
    return milliliters * VOLUME_CONVERSION_FACTOR

if __name__ == '__main__':
    sample_volume_ml = 250
    result_fluid_ounces = convert_milliliters_to_fluid_ounces(sample_volume_ml)
    print(result_fluid_ounces)