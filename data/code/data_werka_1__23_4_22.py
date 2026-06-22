def compare_strings(str1, str2):
    if str1 < str2:
        lex_result = -1
    elif str1 > str2:
        lex_result = 1
    else:
        lex_result = 0
    len_diff = abs(len(str1) - len(str2))
    return (lex_result, len_diff)
if __name__ == '__main__':
    sample_str1 = 'apple'
    sample_str2 = 'banana'
    result = compare_strings(sample_str1, sample_str2)
    print(result)