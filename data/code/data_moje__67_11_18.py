LITERS_TO_MILLILITERS = 1000

def convert_to_milliliters(value_in_liters):
    return value_in_liters * LITERS_TO_MILLILITERS

if __name__ == '__main__':
    samples = [1, 2.5, 0.5]
    for sample in samples:
        result = convert_to_milliliters(sample)
        print(result)