def compare_lengths(length1, length2):
    difference = length1 - length2
    ratio = length1 / length2 if length2 != 0 else float('inf')
    greater = length1 > length2
    return difference, ratio, greater

if __name__ == '__main__':
    sample_length1 = 10.5
    sample_length2 = 5.25
    result = compare_lengths(sample_length1, sample_length2)
    print(result)