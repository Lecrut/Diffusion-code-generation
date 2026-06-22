LITERS_TO_MILLILITERS = 1000

def convert_liters_to_milliliters(value):
    return value * LITERS_TO_MILLILITERS

if __name__ == '__main__':
    sample_values = [1.5, 0.25, 10, 0.001]
    for val in sample_values:
        result = convert_liters_to_milliliters(val)
        print(f"{val} liters is {result} milliliters")