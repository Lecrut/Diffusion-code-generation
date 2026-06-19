def compare_lengths(length1, length2):
    return (min(length1, length2), max(length1, length2))

if __name__ == '__main__':
    sample_length_a = 75
    sample_length_b = 40
    result = compare_lengths(sample_length_a, sample_length_b)
    print(result)