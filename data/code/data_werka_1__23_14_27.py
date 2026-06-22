LEXICOGRAPHIC_EQUAL = 0
LEXICOGRAPHIC_FIRST_IS_GREATER = 1
LEXICOGRAPHIC_SECOND_IS_GREATER = -1

def lexicographic_compare(str1, str2):
    if str1 < str2:
        return LEXICOGRAPHIC_SECOND_IS_GREATER
    elif str1 > str2:
        return LEXICOGRAPHIC_FIRST_IS_GREATER
    else:
        return LEXICOGRAPHIC_EQUAL

if __name__ == '__main__':
    sample_string1 = "orange"
    sample_string2 = "grape"
    comparison_result = lexicographic_compare(sample_string1, sample_string2)
    print(comparison_result)