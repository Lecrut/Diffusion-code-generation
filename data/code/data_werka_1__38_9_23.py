def find_repeated_letters(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")

    repeated_letters = []
    seen_letters = set()

    for char in input_string:
        lower_char = char.lower()
        if lower_char.isalpha():
            if lower_char in seen_letters and lower_char not in repeated_letters:
                repeated_letters.append(lower_char)
            else:
                seen_letters.add(lower_char)

    return repeated_letters

if __name__ == '__main__':
    sample_input = "hello world"
    try:
        result = find_repeated_letters(sample_input)
        print(result)
    except ValueError as e:
        print(e)