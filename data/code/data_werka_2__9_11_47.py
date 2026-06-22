VOLUME_CONVERSION_FACTOR = 1000

def convert_liters_to_milliliters(liters):
    return liters * VOLUME_CONVERSION_FACTOR

if __name__ == '__main__':
    sample_liters = 4.3
    milliliters = convert_liters_to_milliliters(sample_liters)
    print(milliliters)