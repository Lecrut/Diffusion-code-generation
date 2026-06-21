def compare_lengths(length1, length2):
    if length1 > length2:
        return length1
    else:
        return length2

if __name__ == '__main__':
    sample_length1 = 10.5
    sample_length2 = 7.8
    longer_length = compare_lengths(sample_length1, sample_length2)
    print(longer_length)