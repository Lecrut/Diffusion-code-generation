def compare_strings(str1, str2):
    normalized_str1 = str1.lower()
    normalized_str2 = str2.lower()
    return normalized_str1 == normalized_str2

if __name__ == '__main__':
    sample_string_1 = "Alibaba"
    sample_string_2 = "alibaba"
    comparison_result = compare_strings(sample_string_1, sample_string_2)
    print(comparison_result)