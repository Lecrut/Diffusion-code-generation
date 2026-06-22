LITERS_TO_MILLILITERS = 1000

def convert_liters_to_milliliters(value):
    return value * LITERS_TO_MILLILITERS

if __name__ == '__main__':
    samples = [0, 1, 0.5, 2.5, -1.2]
    for s in samples:
        print(convert_liters_to_milliliters(s))