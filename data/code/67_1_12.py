LITERS_TO_MILLILITERS = 1000

def convert_liters_to_milliliters(liters):
    return liters * LITERS_TO_MILLILITERS

if __name__ == '__main__':
    sample_liters = [1, 2.5, 10, 0.5]
    for liters in sample_liters:
        result = convert_liters_to_milliliters(liters)
        print(result)