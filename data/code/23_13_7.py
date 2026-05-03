def compare_strings(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    min_len = min(len1, len2)
    diff_index = -1
    for i in range(min_len):
        if str1[i] != str2[i]:
            diff_index = i
            break
    if diff_index == -1:
        length_diff = len1 - len2
        return {
            "str1": str1,
            "str2": str2,
            "lengths_diff": length_diff,
            "first_diff_index": -1
        }
    else:
        return {
            "str1": str1,
            "str2": str2,
            "lengths_diff": len1 - len2,
            "first_diff_index": diff_index
        }
if __name__ == '__main__':
    s1 = "apple"
    s2 = "apply"
    result1 = compare_strings(s1, s2)
    print(result1)
    s3 = "cat"
    s4 = "dog"
    result2 = compare_strings(s3, s4)
    print(result2)
    s5 = "hello"
    s6 = "hell"
    result3 = compare_strings(s5, s6)
    print(result3)
    s7 = "abc"
    s8 = "abc"
    result4 = compare_strings(s7, s8)
    print(result4)
    s9 = "a"
    s10 = "ab"
    result5 = compare_strings(s9, s10)
    print(result5)