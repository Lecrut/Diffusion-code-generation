def compare_strings(s1, s2):
    if s1 < s2:
        lexicographic_result = -1
    elif s1 > s2:
        lexicographic_result = 1
    else:
        lexicographic_result = 0
    length_difference = len(s1) - len(s2)
    return (lexicographic_result, length_difference)
if __name__ == '__main__':
    sample_string1 = 'apple'
    sample_string2 = 'banana'
    result = compare_strings(sample_string1, sample_string2)
    print(result)