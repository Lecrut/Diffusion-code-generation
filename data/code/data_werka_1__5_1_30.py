def compare_lengths(length1, length2):
    if length1 > length2:
        return ('greater', 'less')
    elif length1 < length2:
        return ('less', 'greater')
    else:
        return ('equal', 'equal')

if __name__ == '__main__':
    sample_length1 = 5.5
    sample_length2 = 3.3
    result = compare_lengths(sample_length1, sample_length2)
    print(result)