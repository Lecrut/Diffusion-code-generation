def compare_strings(str1, str2):
    return (str1 > str2) - (str1 < str2)

if __name__ == '__main__':
    sample_str1 = "apple"
    sample_str2 = "banana"
    comparison_result = compare_strings(sample_str1, sample_str2)
    print(comparison_result)