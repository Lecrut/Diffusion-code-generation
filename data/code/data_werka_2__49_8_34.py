def compare_lengths(length1, length2):
    return (min(length1, length2), max(length1, length2))

if __name__ == '__main__':
    sample_length1 = 15
    sample_length2 = 25
    result = compare_lengths(sample_length1, sample_length2)
    print(result)