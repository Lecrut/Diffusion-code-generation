def run_length_encode(input_string):
    if not input_string:
        return ""

    encoded_chars = []
    count = 1
    current_char = input_string[0]

    for i in range(1, len(input_string)):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            encoded_chars.append(f"{count}{current_char}")
            current_char = char
            count = 1

    encoded_chars.append(f"{count}{current_char}")

    return "".join(encoded_chars)

if __name__ == "__main__":
    sample_input = "aaabbbcc"
    result = run_length_encode(sample_input)
    print(result)

    empty_input = ""
    empty_result = run_length_encode(empty_input)
    print(empty_result)

    single_input = "a"
    single_result = run_length_encode(single_input)
    print(single_result)

    none_input = None
    if none_input is None:
        none_input = ""
    none_result = run_length_encode(none_input)
    print(none_result)