def grams_to_ounces(grams):
    conversion_factor = 1 / 28.3495
    return [g * conversion_factor for g in grams]

if __name__ == '__main__':
    sample_weights = [100, 200, 300]
    converted_weights = grams_to_ounces(sample_weights)
    print(converted_weights)