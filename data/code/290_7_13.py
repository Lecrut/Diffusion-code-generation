def grams_to_milligrams(weight_grams):
    return int(weight_grams * 1000)
if __name__ == '__main__':
    sample_weight = 5000
    converted_weight = grams_to_milligrams(sample_weight)
    print(converted_weight)