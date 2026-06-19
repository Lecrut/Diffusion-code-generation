def compare_strings(str1, str2):
    if str1 < str2:
        comparison_result = 'str1 is less than str2'
    elif str1 > str2:
        comparison_result = 'str1 is greater than str2'
    else:
        comparison_result = 'str1 is equal to str2'
    length_difference = len(str1) - len(str2)
    return (comparison_result, length_difference)
if __name__ == '__main__':
    sample_str1 = 'apple'
    sample_str2 = 'banana'
    result = compare_strings(sample_str1, sample_str2)
    print(result)