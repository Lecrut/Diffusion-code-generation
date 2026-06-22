CONVERSION_FACTOR = 1000.0

def liters_to_milliliters(liters):
    return liters * CONVERSION_FACTOR

if __name__ == '__main__':
    volume_liters = 5.0
    result = liters_to_milliliters(volume_liters)
    print(result)