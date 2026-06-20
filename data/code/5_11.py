def compare_lengths(length1, length2):
    difference = length1 - length2
    ratio = length1 / length2 if length2 != 0 else 0.0
    is_greater = length1 > length2
    return difference, ratio, is_greater

if __name__ == '__main__':
    sample_length1 = 10.5
    sample_length2 = 4.2
    diff, ratio, greater = compare_lengths(sample_length1, sample_length2)
    print(diff)
    print(ratio)
    print(greater)