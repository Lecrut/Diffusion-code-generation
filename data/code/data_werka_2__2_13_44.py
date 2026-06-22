MILLILITERS_TO_FLUID_OUNCES = 0.033814

def scale_volume(milliliters):
    if milliliters < 0:
        raise ValueError("Volume cannot be negative")
    return milliliters * MILLILITERS_TO_FLUID_OUNCES

if __name__ == '__main__':
    sample_value = 1000
    result = scale_volume(sample_value)
    print(result)