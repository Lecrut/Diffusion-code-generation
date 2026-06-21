def compare_strings(str1, str2):
    comparison = {'length_difference': len(str1) - len(str2), 'first_differing_index': None}
    min_length = min(len(str1), len(str2))
    for i in range(min_length):
        if str1[i] != str2[i]:
            comparison['first_differing_index'] = i
            break
    if comparison['first_differing_index'] is None and len(str1) != len(str2):
        comparison['first_differing_index'] = min_length
    return comparison
if __name__ == '__main__':
    str1 = 'hello'
    str2 = 'helium'
    result = compare_strings(str1, str2)
    print(result)