def generate_substrings(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    n = len(s)
    for start in range(n):
        for end in range(start + 1, n + 1):
            yield s[start:end]

if __name__ == '__main__':
    test_string = "hello"
    try:
        substrings_gen = generate_substrings(test_string)
        result = list(substrings_gen)
        print(result)
    except ValueError as e:
        print(e)

    test_string_long = "abcdefghijklmnopqrstuvwxyz"
    try:
        substrings_gen_long = generate_substrings(test_string_long)
        for substring in substrings_gen_long:
            print(substring)
    except ValueError as e:
        print(e)