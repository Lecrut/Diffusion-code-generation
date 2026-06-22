def compare_lengths(length1, length2):
    if length1 > length2:
        return ('greater', length1)
    elif length1 < length2:
        return ('less', length2)
    else:
        return ('equal', length1)

if __name__ == '__main__':
    sample_length1 = 5.7
    sample_length2 = 3.2
    result = compare_lengths(sample_length1, sample_length2)
    print(result)