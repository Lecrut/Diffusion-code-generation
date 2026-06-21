def milliliters_to_fluid_ounces(milliliters):
    conversion_factor = 0.0338140227
    return milliliters * conversion_factor
if __name__ == '__main__':
    sample_volume_ml = 500
    converted_volume_oz = milliliters_to_fluid_ounces(sample_volume_ml)
    print(converted_volume_oz)