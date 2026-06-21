def compare_strings(str1, str2):
    length_diff = len(str1) - len(str2)
    min_length = min(len(str1), len(str2))
    first_diff_index = None

    for i in range(min_length):
        if str1[i] != str2[i]:
            first_diff_index = i
            break

    if first_diff_index is None and length_diff == 0:
        first_diff_index = -1

    return {'length_difference': length_diff, 'first_differing_index': first_diff_index}

if __name__ == '__main__':
    sample_str1 = 'banana'
    sample_str2 = 'bananas'
    comparison_result = compare_strings(sample_str1, sample_str2)
    print(comparison_result)