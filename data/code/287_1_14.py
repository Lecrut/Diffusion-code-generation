def grams_to_ounces(grams):
    return [g / 28.3495 for g in grams]

if __name__ == '__main__':
    sample_weights_grams = [100, 150, 200, 250, 300]
    converted_weights_ounces = grams_to_ounces(sample_weights_grams)
    print(converted_weights_ounces)