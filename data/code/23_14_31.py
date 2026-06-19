LEXY_COMPARE_RESULT_LESS = -1
LEXY_COMPARE_RESULT_EQUAL = 0
LEXY_COMPARE_RESULT_GREATER = 1

def lexicographic_compare(str1, str2):
    if str1 < str2:
        return LEXY_COMPARE_RESULT_LESS
    elif str1 > str2:
        return LEXY_COMPARE_RESULT_GREATER
    else:
        return LEXY_COMPARE_RESULT_EQUAL

if __name__ == '__main__':
    string1 = "orange"
    string2 = "grape"
    result = lexicographic_compare(string1, string2)
    print(result)