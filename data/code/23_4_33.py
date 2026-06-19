def compare_strings(str1, str2):
    if str1 < str2:
        lexical_comparison = -1
    elif str1 > str2:
        lexical_comparison = 1
    else:
        lexical_comparison = 0
    length_difference = abs(len(str1) - len(str2))
    return (lexical_comparison, length_difference)
if __name__ == '__main__':
    sample_str1 = 'apple'
    sample_str2 = 'banana'
    result = compare_strings(sample_str1, sample_str2)
    print(result)