def run_length_encode(input_string: str) -> str:
    if not input_string:
        return ""

    encoded_chars = []
    current_char = input_string[0]
    count = 1

    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_chars.append(f"{count}{current_char}")
            current_char = char
            count = 1

    encoded_chars.append(f"{count}{current_char}")
    return "".join(encoded_chars)

if __name__ == "__main__":
    sample_text = "aaabbc"
    result = run_length_encode(sample_text)
    print(result)