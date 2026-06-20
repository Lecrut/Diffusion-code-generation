def compare_lengths(len1, len2):
    if len1 == len2:
        return 'equal'
    elif len1 > len2:
        return 'len1 is greater'
    else:
        return 'len2 is smaller'

if __name__ == '__main__':
    print(compare_lengths(5, 3))
    print(compare_lengths(2, 8))
    print(compare_lengths(4, 4))