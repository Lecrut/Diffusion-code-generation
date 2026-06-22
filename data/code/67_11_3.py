LITERS_TO_MILLILITERS = 1000

def convert_liters_to_milliliters(value):
    return value * LITERS_TO_MILLILITERS

if __name__ == '__main__':
    sample_values = [1, 2.5, 0.001, 100]
    for v in sample_values:
        result = convert_liters_to_milliliters(v)
        print(result)