LITERS_TO_MILLILITERS = 1000

def liters_to_milliliters(liters):
    return liters * LITERS_TO_MILLILITERS

if __name__ == '__main__':
    sample_liters = [1, 2.5, 0.5, 10]
    for liters in sample_liters:
        print(liters_to_milliliters(liters))