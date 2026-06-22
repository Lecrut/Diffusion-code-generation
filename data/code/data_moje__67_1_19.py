LITER_TO_MILLILITER = 1000

def liters_to_milliliters(liters):
    return liters * LITER_TO_MILLILITER

if __name__ == '__main__':
    sample_liters = [1, 2.5, 0.5, 10]
    for liters in sample_liters:
        result = liters_to_milliliters(liters)
        print(result)