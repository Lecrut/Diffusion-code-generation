def milliliters_to_fluid_ounces(milliliters):
    conversion_factor = 0.0338140226
    return milliliters * conversion_factor
if __name__ == '__main__':
    sample_milliliters = 500
    result = milliliters_to_fluid_ounces(sample_milliliters)
    print(result)