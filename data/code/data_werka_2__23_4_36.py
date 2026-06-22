LEXICAL_COMPARISON_LESS = -1
LEXICAL_COMPARISON_EQUAL = 0
LEXICAL_COMPARISON_GREATER = 1

def compare_strings(str1, str2):
    if str1 < str2:
        lexical_result = LEXICAL_COMPARISON_LESS
    elif str1 > str2:
        lexical_result = LEXICAL_COMPARISON_GREATER
    else:
        lexical_result = LEXICAL_COMPARISON_EQUAL
    
    length_difference = len(str1) - len(str2)
    return (lexical_result, length_difference)

if __name__ == '__main__':
    sample_str1 = 'orange'
    sample_str2 = 'grape'
    result = compare_strings(sample_str1, sample_str2)
    print(result)