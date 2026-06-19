def compare_lengths(len1, len2):
    if len1 == len2:
        return 'equal'
    elif len1 > len2:
        return 'len1 is greater'
    else:
        return 'len2 is smaller'

if __name__ == '__main__':
    length_a = 75
    length_b = 30
    comparison_result = compare_lengths(length_a, length_b)
    print(comparison_result)