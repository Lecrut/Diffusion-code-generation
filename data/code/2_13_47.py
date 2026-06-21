def milliliters_to_fluid_ounces(milliliters):
    return milliliters * 0.033814

if __name__ == '__main__':
    sample_values = [100, 250, 500, 1000]
    for value in sample_values:
        print(f"{value} ml is {milliliters_to_fluid_ounces(value):.2f} fl oz")