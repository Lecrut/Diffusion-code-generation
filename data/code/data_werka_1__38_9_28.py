def find_repeated_letters(input_string):
    seen = set()
    repeated = set()
    for char in input_string:
        if char.isalpha():
            lower_char = char.lower()
            if lower_char in seen:
                repeated.add(lower_char)
            else:
                seen.add(lower_char)
    return list(repeated)

if __name__ == '__main__':
    sample_input = "Alibaba Cloud is a great platform for developers."
    result = find_repeated_letters(sample_input)
    print(result)