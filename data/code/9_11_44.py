def convert_liters_to_milliliters(liters):
    conversion_factor = 1000
    milliliters = liters * conversion_factor
    return milliliters

if __name__ == '__main__':
    sample_volume_liters = 2.5
    converted_volume_milliliters = convert_liters_to_milliliters(sample_volume_liters)
    print(converted_volume_milliliters)