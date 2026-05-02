def generate_substrings(s):
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            yield s[i:j]
if __name__ == '__main__':
    input_string = "abc"
    substring_generator = generate_substrings(input_string)
    all_substrings = list(substring_generator)
    print(all_substrings)
    input_string_long = "abcdefg"
    substring_generator_long = generate_substrings(input_string_long)
    all_substrings_long = list(substring_generator_long)
    print(all_substrings_long)