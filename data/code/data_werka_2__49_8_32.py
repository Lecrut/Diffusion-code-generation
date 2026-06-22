def compare_lengths(length1, length2):
    min_len = length1 if length1 < length2 else length2
    max_len = length1 if length1 > length2 else length2
    return (min_len, max_len)

if __name__ == '__main__':
    sample_length1 = 40
    sample_length2 = 60
    result = compare_lengths(sample_length1, sample_length2)
    print(result)