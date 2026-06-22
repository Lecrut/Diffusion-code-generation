LITER_TO_MILLILITER = 1000

def convert_liters_to_milliliters(value):
    return value * LITER_TO_MILLILITER

if __name__ == '__main__':
    sample_values = [1.5, 10, 0.001]
    for val in sample_values:
        result = convert_liters_to_milliliters(val)
        print(result)