import sys
def compare_strings(str1, str2):
    if str1 == str2:
        return True
    return False
if __name__ == '__main__':
    string_a = "hello"
    string_b = "hello"
    string_c = "world"
    string_d = "hello"
    print(f"Comparing '{string_a}' and '{string_b}': {compare_strings(string_a, string_b)}")
    print(f"Comparing '{string_a}' and '{string_c}': {compare_strings(string_a, string_c)}")
    print(f"Comparing '{string_d}' and '{string_a}': {compare_strings(string_d, string_a)}")