def compare_lengths(length1, length2):
    min_length = length1 if length1 < length2 else length2
    max_length = length1 if length1 > length2 else length2
    return (min_length, max_length)

if __name__ == '__main__':
    sample_length1 = 50
    sample_length2 = 25
    result = compare_lengths(sample_length1, sample_length2)
    print(result)