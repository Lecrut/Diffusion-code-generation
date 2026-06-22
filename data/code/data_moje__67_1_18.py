CONVERSION_FACTOR = 1000

def convert_liter_to_milliliter(volume_in_liters):
    return volume_in_liters * CONVERSION_FACTOR

if __name__ == '__main__':
    liters = 1.5
    milliliters = convert_liter_to_milliliter(liters)
    print(milliliters)