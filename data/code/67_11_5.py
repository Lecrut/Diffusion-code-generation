LITER_TO_MILLILITER = 1000

def convert_liters_to_milliliters(value):
    return value * LITER_TO_MILLILITER

if __name__ == '__main__':
    sample_values = [1.0, 2.5, 0.001]
    for val in sample_values:
        result = convert_liters_to_milliliters(val)
        print(f"{val} liters is {result} milliliters")