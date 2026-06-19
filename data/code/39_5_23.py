def generate_substrings(s):
    n = len(s)
    for start in range(n):
        for end in range(start + 1, n + 1):
            yield s[start:end]

if __name__ == '__main__':
    test_string = "hello"
    substrings_gen = generate_substrings(test_string)
    result = list(substrings_gen)
    print(result)
    
    test_string_long = "abcdefghijklmnopqrstuvwxyz"
    substrings_gen_long = generate_substrings(test_string_long)
    for sub in substrings_gen_long:
        print(sub)