def compare_strings(str1, str2):
    lex_comparison = 0
    if str1 < str2:
        lex_comparison = -1
    elif str1 > str2:
        lex_comparison = 1
    else:
        lex_comparison = 0
    len_difference = len(str1) - len(str2)
    return (lex_comparison, len_difference)
if __name__ == '__main__':
    s1 = "apple"
    s2 = "apply"
    result1 = compare_strings(s1, s2)
    print(f"Comparing '{s1}' and '{s2}': {result1}")
    s3 = "banana"
    s4 = "apple"
    result2 = compare_strings(s3, s4)
    print(f"Comparing '{s3}' and '{s4}': {result2}")
    s5 = "test"
    s6 = "testing"
    result3 = compare_strings(s5, s6)
    print(f"Comparing '{s5}' and '{s6}': {result3}")
    s7 = "hello"
    s8 = "hello"
    result4 = compare_strings(s7, s8)
    print(f"Comparing '{s7}' and '{s8}': {result4}")