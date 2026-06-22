LITER_TO_MILLILITER = 1000.0

def convert_liters_to_milliliters(liters):
    return liters * LITER_TO_MILLILITER

if __name__ == '__main__':
    sample_liters = 5.5
    result = convert_liters_to_milliliters(sample_liters)
    print(result)