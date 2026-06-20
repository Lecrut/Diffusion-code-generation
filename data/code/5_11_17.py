def compare_lengths(length1, length2):
    difference = length1 - length2
    ratio = length1 / length2 if length2 != 0 else float('inf') if length1 != 0 else 0.0
    is_greater = length1 > length2
    return difference, ratio, is_greater

if __name__ == '__main__':
    length_a = 10.5
    length_b = 7.2
    result = compare_lengths(length_a, length_b)
    print(result)