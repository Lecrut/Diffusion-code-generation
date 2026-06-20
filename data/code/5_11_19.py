def compare_lengths(length1, length2):
    difference = length1 - length2
    if length2 == 0:
        raise ZeroDivisionError("length2 cannot be zero for ratio calculation")
    ratio = length1 / length2
    is_greater = length1 > length2
    return difference, ratio, is_greater

if __name__ == '__main__':
    length1 = 10.5
    length2 = 7.3
    result = compare_lengths(length1, length2)
    print(result)