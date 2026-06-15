def compare_strings(str1, str2):
    s1_lower = str1.lower()
    s2_lower = str2.lower()
    if s1_lower > s2_lower:
        return str1
    elif s2_lower > s1_lower:
        return str2
    else:
        return str1 if str1 > str2 else str2
if __name__ == '__main__':
    string_a = "Apple"
    string_b = "banana"
    result = compare_strings(string_a, string_b)
    print(result)
    string_c = "Zebra"
    string_d = "ant"
    result2 = compare_strings(string_c, string_d)
    print(result2)
    string_e = "Cat"
    string_f = "dog"
    result3 = compare_strings(string_e, string_f)
    print(result3)
    string_g = "aBc"
    string_h = "abc"
    result4 = compare_strings(string_g, string_h)
    print(result4)