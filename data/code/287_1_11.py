def grams_to_ounces(grams):
    ounces = [g / 28.3495 for g in grams]
    return ounces

if __name__ == '__main__':
    sample_weights = [100, 200, 300, 400]
    converted_weights = grams_to_ounces(sample_weights)
    print(converted_weights)