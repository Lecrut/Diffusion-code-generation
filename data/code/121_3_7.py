def compare_strings(str1, str2):
    return -1 if str1 < str2 else (1 if str1 > str2 else 0)

if __name__ == '__main__':
    string_a = "hello"
    string_b = "world"
    result = compare_strings(string_a, string_b)
    print(result)