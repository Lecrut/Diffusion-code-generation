LITER_TO_MILLILITER_FACTOR = 1000

def convert_liters_to_milliliters(liters):
    return liters * LITER_TO_MILLILITER_FACTOR

if __name__ == '__main__':
    sample_values = [1, 2.5, 10, 0.001]
    for value in sample_values:
        result = convert_liters_to_milliliters(value)
        print(result)