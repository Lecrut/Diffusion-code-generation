def lexicographic_compare(str1, str2):
    if str1 < str2:
        return -1
    elif str1 > str2:
        return 1
    else:
        return 0

if __name__ == '__main__':
    sample_string1 = "orange"
    sample_string2 = "grape"
    comparison_result = lexicographic_compare(sample_string1, sample_string2)
    print(comparison_result)