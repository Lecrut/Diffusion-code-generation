def compare_strings(str1, str2):
    lexical_result = 0 if str1 == str2 else (-1 if str1 < str2 else 1)
    length_difference = len(str1) - len(str2)
    return (lexical_result, length_difference)

if __name__ == '__main__':
    sample_str1 = 'orange'
    sample_str2 = 'grapefruit'
    result = compare_strings(sample_str1, sample_str2)
    print(result)