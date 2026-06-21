def milliliters_to_fluid_ounces(milliliters):
    return milliliters * 0.033814

if __name__ == '__main__':
    sample_value = 500
    result = milliliters_to_fluid_ounces(sample_value)
    print(result)