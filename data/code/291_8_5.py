def recursive_length_compare(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 == 0 and len2 == 0:
        return 0
    elif len1 == 0:
        return len2
    elif len2 == 0:
        return len1
    else:
        return abs(len1 - len2)
if __name__ == '__main__':
    string_a = "hello"
    string_b = "world"
    result1 = recursive_length_compare(string_a, string_b)
    print(f"Comparing '{string_a}' and '{string_b}': {result1}")
    string_c = "recursion"
    string_d = "recursively"
    result2 = recursive_length_compare(string_c, string_d)
    print(f"Comparing '{string_c}' and '{string_d}': {result2}")
    string_e = ""
    string_f = "test"
    result3 = recursive_length_compare(string_e, string_f)
    print(f"Comparing '{string_e}' and '{string_f}': {result3}")
    string_g = "abc"
    string_h = "abc"
    result4 = recursive_length_compare(string_g, string_h)
    print(f"Comparing '{string_g}' and '{string_h}': {result4}")