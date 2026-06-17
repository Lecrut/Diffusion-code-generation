import sys
def compare_strings(str1, str2):
    return str1 == str2
if __name__ == '__main__':
    string_a = "hello"
    string_b = "hello"
    string_c = "world"
    result1 = compare_strings(string_a, string_b)
    print(f"Comparing '{string_a}' and '{string_b}': {result1}")
    result2 = compare_strings(string_a, string_c)
    print(f"Comparing '{string_a}' and '{string_c}': {result2}")