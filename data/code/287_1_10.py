def grams_to_ounces(grams):
    return [g / 28.3495 for g in grams]

if __name__ == '__main__':
    sample_weights_grams = [100, 200, 300, 400]
    weights_in_ounces = grams_to_ounces(sample_weights_grams)
    print(weights_in_ounces)