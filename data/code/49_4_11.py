def find_length_ratio(length1, length2):
    smaller_length = min(length1, length2)
    larger_length = max(length1, length2)
    ratio_of_lengths = larger_length / smaller_length
    return ratio_of_lengths

if __name__ == '__main__':
    sample_length_a = 7
    sample_length_b = 14
    computed_ratio = find_length_ratio(sample_length_a, sample_length_b)
    print(computed_ratio)