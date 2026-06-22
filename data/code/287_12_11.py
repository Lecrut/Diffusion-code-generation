CONVERSION_FACTOR = 28.3495

def grams_to_ounces(grams):
    return [g / CONVERSION_FACTOR for g in grams]

if __name__ == '__main__':
    sample_weights = [100, 200, 300]
    print(grams_to_ounces(sample_weights))