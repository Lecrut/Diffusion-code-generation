def compare_lengths(len1, len2):
    if len1 == len2:
        return 'equal'
    elif len1 > len2:
        return 'len1 is greater'
    else:
        return 'len2 is smaller'

if __name__ == '__main__':
    length1 = 50
    length2 = 75
    result = compare_lengths(length1, length2)
    print(result)