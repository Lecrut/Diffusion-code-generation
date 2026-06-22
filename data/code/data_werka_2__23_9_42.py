def compare_strings(str1, str2):
    length_diff = len(str1) - len(str2)
    min_length = min(len(str1), len(str2))
    
    for i in range(min_length):
        if str1[i] != str2[i]:
            return {'length_difference': length_diff, 'first_differing_index': i}
    
    if length_diff == 0:
        return {'length_difference': length_diff, 'first_differing_index': -1}
    else:
        return {'length_difference': length_diff, 'first_differing_index': min_length}

if __name__ == '__main__':
    str1 = 'hello'
    str2 = 'helium'
    result = compare_strings(str1, str2)
    print(result)