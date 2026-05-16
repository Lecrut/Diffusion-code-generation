def combine_strings(str1, str2):
    combined = str1 + str2
    reversed = str2 + str1
    return combined, reversed
if __name__ == '__main__':
    string_a = "hello"
    string_b = "world"
    result1, result2 = combine_strings(string_a, string_b)
    print(f"Combined: {result1}")
    print(f"Reversed: {result2}")
    string_c = "Python"
    string_d = "code"
    result3, result4 = combine_strings(string_c, string_d)
    print(f"Combined: {result3}")
    print(f"Reversed: {result4}")