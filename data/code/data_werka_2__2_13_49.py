def milliliters_to_fluid_ounces(milliliters):
    return milliliters / 29.5735
if __name__ == '__main__':
    sample_milliliters = 500
    result = milliliters_to_fluid_ounces(sample_milliliters)
    print(result)