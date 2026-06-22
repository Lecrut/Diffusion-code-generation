def compare_lengths(length1, length2):
    if length1 > length2:
        return ('first', 'greater')
    elif length1 < length2:
        return ('second', 'less')
    else:
        return ('both', 'equal')

if __name__ == '__main__':
    sample_length1 = 5.5
    sample_length2 = 3.3
    result = compare_lengths(sample_length1, sample_length2)
    print(result)