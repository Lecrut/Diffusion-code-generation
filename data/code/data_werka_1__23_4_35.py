def compare_strings(str1, str2):
    if str1 < str2:
        lexicographical_result = -1
    elif str1 > str2:
        lexicographical_result = 1
    else:
        lexicographical_result = 0
    length_difference = abs(len(str1) - len(str2))
    return (lexicographical_result, length_difference)
if __name__ == '__main__':
    sample_str1 = 'apple'
    sample_str2 = 'banana'
    result = compare_strings(sample_str1, sample_str2)
    print(result)