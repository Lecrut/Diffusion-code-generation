def generate_substrings(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            yield s[i:j]

if __name__ == '__main__':
    try:
        test_string = "hello"
        substring_generator = generate_substrings(test_string)
        all_substrings = list(substring_generator)
        print(all_substrings)

        invalid_input = 12345
        substring_generator_invalid = generate_substrings(invalid_input)
    except ValueError as e:
        print(e)