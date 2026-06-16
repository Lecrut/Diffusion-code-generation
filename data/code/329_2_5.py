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
    print(f"Comparing '{string_a}' and '{string_b}': {compare_strings_optimized(string_a, string_b)}")
    print(f"Comparing '{string_a}' and '{string_c}': {compare_strings_optimized(string_a, string_c)}")
    print(f"Comparing '{string_a}' and '{string_d}': {compare_strings_optimized(string_a, string_d)}")
    print(f"Comparing '{string_a}' and '{string_e}': {compare_strings_optimized(string_a, string_e)}")
    string_a_int = 123
    string_b_int = "123"
    print(f"Comparing integer {string_a_int} and string '{string_b_int}': {compare_strings_optimized(string_a_int, string_b_int)}")