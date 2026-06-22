LITER_TO_MILLILITER_FACTOR = 1000

def convert_liters_to_milliliters(liters):
    return liters * LITER_TO_MILLILITER_FACTOR

if __name__ == '__main__':
    sample_liters = 2.5
    result = convert_liters_to_milliliters(sample_liters)
    print(result)