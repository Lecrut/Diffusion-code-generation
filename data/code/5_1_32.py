def compare_lengths(length1, length2):
    if length1 > length2:
        return ('length1', 'greater')
    elif length1 < length2:
        return ('length2', 'greater')
    else:
        return ('both', 'equal')

if __name__ == '__main__':
    length1 = 5.5
    length2 = 3.3
    result = compare_lengths(length1, length2)
    print(result)