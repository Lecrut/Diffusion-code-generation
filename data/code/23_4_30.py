def compare_strings(s1, s2):
    if s1 < s2:
        lex_result = -1
    elif s1 > s2:
        lex_result = 1
    else:
        lex_result = 0
    len_diff = len(s1) - len(s2)
    return (lex_result, len_diff)
if __name__ == '__main__':
    sample_string1 = 'apple'
    sample_string2 = 'banana'
    result = compare_strings(sample_string1, sample_string2)
    print(result)