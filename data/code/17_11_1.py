def run_length_encode(input_string: str) -> str:
    if not input_string:
        return ""

    encoded = []
    current_char = input_string[0]
    count = 1

    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1

    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

if __name__ == "__main__":
    sample_input = "AAABBBCCDAA"
    result = run_length_encode(sample_input)
    print(result)

    sample_input_2 = "ABC"
    result_2 = run_length_encode(sample_input_2)
    print(result_2)

    sample_input_3 = ""
    result_3 = run_length_encode(sample_input_3)
    print(result_3)

    sample_input_4 = "A"
    result_4 = run_length_encode(sample_input_4)
    print(result_4)