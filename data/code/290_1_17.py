def grams_to_ounces(grams):
    ounces = grams * 0.035274
    return "{:.2f}".format(ounces)

if __name__ == '__main__':
    sample_value = 100
    print(grams_to_ounces(sample_value))