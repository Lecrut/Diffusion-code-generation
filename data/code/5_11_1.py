def compare_lengths(length1, length2):
    difference = length1 - length2
    ratio = length1 / length2 if length2 != 0 else float('inf')
    is_greater = length1 > length2
    return difference, ratio, is_greater

if __name__ == '__main__':
    l1 = 10.5
    l2 = 7.2
    result = compare_lengths(l1, l2)
    print(result)