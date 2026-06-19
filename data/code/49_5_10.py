def compare_lengths(len1, len2):
    comparison_map = {
        -1: 'len1 is smaller',
        0: 'equal',
        1: 'len1 is greater'
    }
    result_key = (len1 > len2) - (len1 < len2)
    return comparison_map[result_key]

if __name__ == '__main__':
    length1 = 35
    length2 = 35
    result = compare_lengths(length1, length2)
    print(result)