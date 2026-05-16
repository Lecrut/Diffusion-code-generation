def combine_strings(str1, str2):
    combined = str1 + str2
    reversed = str2 + str1
    return combined, reversed
if __name__ == '__main__':
    string_a = "hello"
    string_b = "world"
    result1, result2 = combine_strings(string_a, string_b)
    print(f"String A: {string_a}")
    print(f"String B: {string_b}")
    print(f"Combined (A then B): {result1}")
    print(f"Combined (B then A): {result2}")
    string_c = "Python"
    string_d = "module"
    result3, result4 = combine_strings(string_c, string_d)
    print(f"\nString C: {string_c}")
    print(f"String D: {string_d}")
    print(f"Combined (C then D): {result3}")
    print(f"Combined (D then C): {result4}")