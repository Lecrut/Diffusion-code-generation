def grams_to_ounces(grams):
    ounces = [g / 28.3495 for g in grams]
    return ounces

if __name__ == '__main__':
    weights_in_grams = [100, 200, 300, 400, 500]
    converted_weights = grams_to_ounces(weights_in_grams)
    print(converted_weights)