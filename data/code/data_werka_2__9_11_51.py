VOLUME_CONVERSION_FACTOR = 1000

def convert_liters_to_milliliters(liters):
    if not isinstance(liters, (int, float)):
        raise ValueError("Volume in liters must be a number")
    return liters * VOLUME_CONVERSION_FACTOR

if __name__ == '__main__':
    sample_liters = 4.0
    milliliters = convert_liters_to_milliliters(sample_liters)
    print(milliliters)