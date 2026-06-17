import sys
def compare_strings_optimized(str1, str2):
    if str1 == str2:
        return True
    return False
if __name__ == '__main__':
    string_a = "hello"
    string_b = "hello"
    string_c = "world"
    print(f"Comparing '{string_a}' and '{string_b}': {compare_strings_optimized(string_a, string_b)}")
    print(f"Comparing '{string_a}' and '{string_c}': {compare_strings_optimized(string_a, string_c)}")