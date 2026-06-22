LITERS_TO_MILLILITERS = 1000

def convert_liters_to_milliliters(value):
    return value * LITERS_TO_MILLILITERS

if __name__ == '__main__':
    sample_value = 2.5
    result = convert_liters_to_milliliters(sample_value)
    print(result)