def compare_strings(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    min_len = min(len1, len2)
    diff_index = -1
    for i in range(min_len):
        if str1[i] != str2[i]:
            diff_index = i
            break
    return {
        "str1": str1,
        "str2": str2,
        "length_diff": len1 - len2,
        "first_diff_index": diff_index
    }
if __name__ == '__main__':
    string_a = "apple"
    string_b = "apply"
    comparison_result = compare_strings(string_a, string_b)
    print(comparison_result)
    string_c = "banana"
    string_d = "bandana"
    comparison_result = compare_strings(string_c, string_d)
    print(comparison_result)
    string_e = "cat"
    string_f = "dog"
    comparison_result = compare_strings(string_e, string_f)
    print(comparison_result)
    string_g = "hello"
    string_h = "hell"
    comparison_result = compare_strings(string_g, string_h)
    print(comparison_result)