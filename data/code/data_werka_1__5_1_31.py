def compare_lengths(a, b):
    if a > b:
        return ('first', 'greater')
    elif a < b:
        return ('second', 'less')
    else:
        return ('both', 'equal')

if __name__ == '__main__':
    length1 = 3.5
    length2 = 2.8
    result = compare_lengths(length1, length2)
    print(result)