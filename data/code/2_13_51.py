def milliliters_to_fluid_ounces(milliliters):
    conversion_factor = 0.0338140226
    return milliliters * conversion_factor
if __name__ == '__main__':
    sample_values = [100, 250, 500, 1000]
    for value in sample_values:
        result = milliliters_to_fluid_ounces(value)
        print(f'{value} milliliters is {result} fluid ounces')