def grams_to_ounces(grams):
    return grams / 28.3495
if __name__ == '__main__':
    sample_mass = 1000
    result = grams_to_ounces(sample_mass)
    print(result)