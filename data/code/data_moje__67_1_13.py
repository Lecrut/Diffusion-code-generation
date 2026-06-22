CONVERSION_FACTOR = 1000

def convert_liters_to_milliliters(liters):
    return liters * CONVERSION_FACTOR

if __name__ == '__main__':
    liter_inputs = [1.5, 0.5, 10, 0.1]
    for liters in liter_inputs:
        result = convert_liters_to_milliliters(liters)
        print(result)