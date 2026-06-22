CONVERSION_FACTOR = 1000

def grams_to_milligrams(grams):
    return int(grams * CONVERSION_FACTOR)

if __name__ == '__main__':
    sample_weight_grams = 5000
    result_milligrams = grams_to_milligrams(sample_weight_grams)
    print(result_milligrams)