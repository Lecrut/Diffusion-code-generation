def generate_substrings(s):
    n = len(s)
    for start in range(n):
        for end in range(start + 1, n + 1):
            yield s[start:end]

if __name__ == '__main__':
    test_string = "hello"
    print("Substrings of 'hello':")
    for sub in generate_substrings(test_string):
        print(sub)
    
    test_string_long = "abcdefghij"
    print("\nSubstrings of 'abcdefghij':")
    for sub in generate_substrings(test_string_long):
        print(sub)