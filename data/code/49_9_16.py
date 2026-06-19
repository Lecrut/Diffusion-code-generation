def compare_lengths(length1, length2):
    lengths = {'length1': length1, 'length2': length2}
    min_length = min(lengths.values())
    max_length = max(lengths.values())
    return (min_length, max_length)

if __name__ == '__main__':
    sample_length1 = 30
    sample_length2 = 45
    result = compare_lengths(sample_length1, sample_length2)
    print(result)