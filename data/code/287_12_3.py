CONVERSION_TABLE = {
    'g': 1,
    'gram': 1,
    'grams': 1,
    'oz': 28.3495,
    'ounce': 28.3495,
    'ounces': 28.3495
}

def grams_to_ounces(grams):
    return [g / CONVERSION_TABLE['gram'] for g in grams]

if __name__ == '__main__':
    sample_weights = [100, 200, 300]
    print(grams_to_ounces(sample_weights))