def convert_volume(milliliters):
    if milliliters < 0:
        raise ValueError('Volume cannot be negative')
    MILLILITERS_TO_FLUID_OUNCES = 0.033814
    return milliliters * MILLILITERS_TO_FLUID_OUNCES
if __name__ == '__main__':
    sample_value = 250
    try:
        result = convert_volume(sample_value)
        print(result)
    except ValueError as e:
        print(e)