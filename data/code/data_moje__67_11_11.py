LITERS_TO_ML = 1000

def convert_liters_to_milliliters(value):
    return value * LITERS_TO_ML

if __name__ == '__main__':
    result = convert_liters_to_milliliters(2.5)
    print(result)