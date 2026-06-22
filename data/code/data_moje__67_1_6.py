LITER_TO_MILLILITER = 1000

def convert_liters_to_milliliters(liters):
    return liters * LITER_TO_MILLILITER

if __name__ == '__main__':
    sample_liters_1 = 2
    sample_liters_2 = 0.5
    sample_liters_3 = 15
    print(convert_liters_to_milliliters(sample_liters_1))
    print(convert_liters_to_milliliters(sample_liters_2))
    print(convert_liters_to_milliliters(sample_liters_3))