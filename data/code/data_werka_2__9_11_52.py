VOLUME_CONVERSION_FACTOR = 1000

def convert_liters_to_milliliters(liters):
    return liters * VOLUME_CONVERSION_FACTOR

if __name__ == '__main__':
    sample_volume_in_liters = 4.75
    converted_volume = convert_liters_to_milliliters(sample_volume_in_liters)
    print(converted_volume)