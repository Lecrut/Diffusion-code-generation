def compare_strings_case_insensitive(str1, str2):
    lower1 = str1.lower()
    lower2 = str2.lower()
    if lower1 > lower2:
        return str1
    elif lower1 < lower2:
        return str2
    else:
        return str1
if __name__ == '__main__':
    string_a = "Apple"
    string_b = "Banana"
    result1 = compare_strings_case_insensitive(string_a, string_b)
    print(f"Comparing '{string_a}' and '{string_b}': Result is '{result1}'")
    string_c = "Zebra"
    string_d = "antelope"
    result2 = compare_strings_case_insensitive(string_c, string_d)
    print(f"Comparing '{string_c}' and '{string_d}': Result is '{result2}'")
    string_e = "Cat"
    string_f = "dog"
    result3 = compare_strings_case_insensitive(string_e, string_f)
    print(f"Comparing '{string_e}' and '{string_f}': Result is '{result3}'")
    string_g = "Alpha"
    string_h = "beta"
    result4 = compare_strings_case_insensitive(string_g, string_h)
    print(f"Comparing '{string_g}' and '{string_h}': Result is '{result4}'")