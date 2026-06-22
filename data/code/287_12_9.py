def grams_to_ounces(grams):
    return [g / 28.3495 for g in grams]

if __name__ == '__main__':
    sample_weights = [100, 200, 300, 400]
    print(grams_to_ounces(sample_weights))