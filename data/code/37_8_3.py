def combine_strings(str1, str2):
    combined = str1 + str2
    reversed_combined = str2 + str1
    return combined, reversed_combined
if __name__ == '__main__':
    string_a = "hello"
    string_b = "world"
    result1, result2 = combine_strings(string_a, string_b)
    print(f"String A: {string_a}")
    print(f"String B: {string_b}")
    print(f"Combined (A then B): {result1}")
    print(f"Combined (B then A): {result2}")