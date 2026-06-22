def grams_to_milligrams(weight_grams):
    if not isinstance(weight_grams, (int, float)) or weight_grams < 0:
        raise ValueError('Weight must be a non-negative number in grams')
    milligrams = int(weight_grams * 1000)
    return milligrams
if __name__ == '__main__':
    sample_weight = 500
    result = grams_to_milligrams(sample_weight)
    print(result)