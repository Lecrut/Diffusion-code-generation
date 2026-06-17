def compare_strings_optimized(str1, str2):
    if type(str1) is not type(str2):
        return False
    return str1 == str2
if __name__ == '__main__':
    string_a = "hello"
    string_b = "hello"
    string_c = "world"
    string_d = "hello "
    string_e = "hello"
    print(f"'{string_a}' == '{string_b}': {compare_strings_optimized(string_a, string_b)}")
    print(f"'{string_a}' == '{string_c}': {compare_strings_optimized(string_a, string_c)}")
    print(f"'{string_d}' == '{string_e}': {compare_strings_optimized(string_d, string_e)}")