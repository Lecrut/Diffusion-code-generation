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
    str_a = "apple"
    str_b = "apply"
    result1 = recursive_length_compare(str_a, str_b)
    print(f"Comparing '{str_a}' and '{str_b}': {result1}")
    str_c = "banana"
    str_d = "band"
    result2 = recursive_length_compare(str_c, str_d)
    print(f"Comparing '{str_c}' and '{str_d}': {result2}")
    str_e = "hello"
    str_f = "world"
    result3 = recursive_length_compare(str_e, str_f)
    print(f"Comparing '{str_e}' and '{str_f}': {result3}")
    str_g = ""
    str_h = "test"
    result4 = recursive_length_compare(str_g, str_h)
    print(f"Comparing '{str_g}' and '{str_h}': {result4}")
    str_i = "abc"
    str_j = "abc"
    result5 = recursive_length_compare(str_i, str_j)
    print(f"Comparing '{str_i}' and '{str_j}': {result5}")