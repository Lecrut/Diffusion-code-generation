def compare_lengths(length1, length2):
    difference = length1 - length2
    if length2 != 0:
        ratio = length1 / length2
    else:
        ratio = float('inf') if length1 > 0 else float('-inf') if length1 < 0 else 0.0
    is_greater = length1 > length2
    return difference, ratio, is_greater

if __name__ == '__main__':
    val1 = 10.5
    val2 = 7.2
    result = compare_lengths(val1, val2)
    print(result)