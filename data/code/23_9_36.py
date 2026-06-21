def compare_strings(str1, str2):
    length_difference = len(str1) - len(str2)
    first_differing_index = None

    min_length = min(len(str1), len(str2))
    for i in range(min_length):
        if str1[i] != str2[i]:
            first_differing_index = i
            break

    if first_differing_index is None and length_difference == 0:
        first_differing_index = -1

    return {'length_difference': length_difference, 'first_differing_index': first_differing_index}

if __name__ == '__main__':
    str1 = 'example'
    str2 = 'exhibit'
    result = compare_strings(str1, str2)
    print(result)