LITER_TO_MILLILITER_FACTOR = 1000

def convert_liters_to_milliliters(liters):
    return liters * LITER_TO_MILLILITER_FACTOR

if __name__ == '__main__':
    sample_inputs = [1, 2.5, 0.0, 10, -3]
    for liters in sample_inputs:
        result = convert_liters_to_milliliters(liters)
        print(result)