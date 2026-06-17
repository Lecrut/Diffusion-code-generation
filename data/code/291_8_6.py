def recursive_length_compare(s1, s2):
    if not s1 and not s2:
        return 0
    if not s1:
        return len(s2)
    if not s2:
        return len(s1)
    len1 = len(s1)
    len2 = len(s2)
    if len1 == len2:
        return 0
    elif len1 > len2:
        return len1 - len2
    else:
        return len2 - len1
if __name__ == '__main__':
    string_a = "apple"
    string_b = "apply"
    result1 = recursive_length_compare(string_a, string_b)
    print(f"Comparing '{string_a}' and '{string_b}': {result1}")
    string_c = "banana"
    string_d = "band"
    result2 = recursive_length_compare(string_c, string_d)
    print(f"Comparing '{string_c}' and '{string_d}': {result2}")
    string_e = "test"
    string_f = "testing"
    result3 = recursive_length_compare(string_e, string_f)
    print(f"Comparing '{string_e}' and '{string_f}': {result3}")
    string_g = "hello"
    string_h = "world"
    result4 = recursive_length_compare(string_g, string_h)
    print(f"Comparing '{string_g}' and '{string_h}': {result4}")