def compare_lengths(length1, length2):
    if length1 > length2:
        return ('length1', 'greater')
    elif length1 < length2:
        return ('length2', 'greater')
    else:
        return ('equal',)
if __name__ == '__main__':
    result = compare_lengths(3.5, 4.2)
    print(result)
    result = compare_lengths(5.0, 5.0)
    print(result)
    result = compare_lengths(7.8, 6.1)
    print(result)