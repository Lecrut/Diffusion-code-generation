def milliliters_to_fluid_ounces(milliliters):
    return milliliters * 0.033814

if __name__ == '__main__':
    sample_milliliters = 500
    fluid_ounces = milliliters_to_fluid_ounces(sample_milliliters)
    print(fluid_ounces)