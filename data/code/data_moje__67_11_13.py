LITERS_TO_MILLILITERS = 1000.0

def convert_to_milliliters(value_in_liters):
    return value_in_liters * LITERS_TO_MILLILITERS

if __name__ == '__main__':
    sample_liters = 2.5
    result = convert_to_milliliters(sample_liters)
    print(result)