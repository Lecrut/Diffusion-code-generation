def generate_all_substrings(s):
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            yield s[i:j+1]
if __name__ == '__main__':
    input_string = "abc"
    substrings_generator = generate_all_substrings(input_string)
    all_substrings = list(substrings_generator)
    print(all_substrings)
    input_string_long = "abcdefg"
    substrings_generator_long = generate_all_substrings(input_string_long)
    all_substrings_long = list(substrings_generator_long)
    print(f"Length of string: {len(input_string_long)}")
    print(f"Number of substrings: {len(all_substrings_long)}")