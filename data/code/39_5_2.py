def generate_substrings(s):
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            yield s[i:j]
if __name__ == '__main__':
    test_string = "abc"
    substrings = generate_substrings(test_string)
    result = list(substrings)
    print(result)
    test_string_long = "abcdefg"
    substrings_long = generate_substrings(test_string_long)
    result_long = list(substrings_long)
    print(result_long)