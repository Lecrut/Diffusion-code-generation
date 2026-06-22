LITERS_TO_MILLILITERS_FACTOR = 1000

def convert_liters_to_milliliters(liters):
    return liters * LITERS_TO_MILLILITERS_FACTOR

if __name__ == '__main__':
    print(convert_liters_to_milliliters(1))
    print(convert_liters_to_milliliters(2.5))
    print(convert_liters_to_milliliters(0))