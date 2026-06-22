LITER_TO_MILLILITER = 1000

def convert_liters_to_milliliters(liters):
    return liters * LITER_TO_MILLILITER

if __name__ == '__main__':
    sample_inputs = [1, 2.5, 10, 0.05]
    for value in sample_inputs:
        result = convert_liters_to_milliliters(value)
        print(result)