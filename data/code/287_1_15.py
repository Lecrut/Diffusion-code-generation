def grams_to_ounces(grams):
    return [g / 28.3495 for g in grams]

if __name__ == '__main__':
    sample_weights_grams = [100, 200, 300, 400]
    converted_weights_ounces = grams_to_ounces(sample_weights_grams)
    print(converted_weights_ounces)