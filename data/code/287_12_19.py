def grams_to_ounces(grams):
    ounces_per_gram = 1 / 28.3495
    return [g * ounces_per_gram for g in grams]

if __name__ == '__main__':
    sample_weights = [100, 200, 300]
    converted_weights = grams_to_ounces(sample_weights)
    print(converted_weights)