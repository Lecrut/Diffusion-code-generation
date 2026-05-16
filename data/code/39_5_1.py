def generate_all_substrings(s):
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            yield s[i:j+1]
if __name__ == '__main__':
    test_string = "abc"
    print("Substrings of 'abc':")
    for sub in generate_all_substrings(test_string):
        print(sub)
    test_string_long = "abcdefg"
    print("\nSubstrings of 'abcdefg':")
    for sub in generate_all_substrings(test_string_long):
        print(sub)