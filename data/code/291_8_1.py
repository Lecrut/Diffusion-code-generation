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
    print(recursive_length_compare(string_a, string_b))
    string_c = "recursion"
    string_d = "recursively"
    print(recursive_length_compare(string_c, string_d))
    string_e = ""
    string_f = "test"
    print(recursive_length_compare(string_e, string_f))
    string_g = "abc"
    string_h = "abc"
    print(recursive_length_compare(string_g, string_h))