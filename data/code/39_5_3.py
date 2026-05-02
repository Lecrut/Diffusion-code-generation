def generate_substrings(s):
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            yield s[i:j]
if __name__ == '__main__':
    test_string = "abc"
    print("Substrings of 'abc':")
    for sub in generate_substrings(test_string):
        print(sub)
    test_string_long = "abcdefg"
    print("\nSubstrings of 'abcdefg':")
    for sub in generate_substrings(test_string_long):
        print(sub)