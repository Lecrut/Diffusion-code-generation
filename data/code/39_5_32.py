def is_valid_string(s):
    return isinstance(s, str)

def generate_substrings(s):
    if not is_valid_string(s):
        raise ValueError('Input must be a string')
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            yield s[i:j]
if __name__ == '__main__':
    test_string = 'hello'
    substrings_gen = generate_substrings(test_string)
    result = list(substrings_gen)
    print("Substrings of 'hello':")
    for sub in result:
        print(sub)
    test_string_long = 'abcdefghijklmnopqrstuvwxyz'
    substrings_gen_long = generate_substrings(test_string_long)
    result_long = list(substrings_gen_long)
    print("\nSubstrings of 'abcdefghijklmnopqrstuvwxyz':")
    for sub in result_long[:10]:
        print(sub)