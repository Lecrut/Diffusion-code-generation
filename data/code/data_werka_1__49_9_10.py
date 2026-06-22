def compare_lengths(length1, length2):
    return (min(length1, length2), max(length1, length2))

if __name__ == '__main__':
    sample_length1 = 50
    sample_length2 = 75
    result = compare_lengths(sample_length1, sample_length2)
    print(result)