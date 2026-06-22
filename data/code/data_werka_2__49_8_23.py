def compare_lengths(length1, length2):
    if length1 < length2:
        return (length1, length2)
    elif length1 > length2:
        return (length2, length1)
    else:
        return (length1, length1)

if __name__ == '__main__':
    sample_length1 = 30
    sample_length2 = 45
    result = compare_lengths(sample_length1, sample_length2)
    print(result)