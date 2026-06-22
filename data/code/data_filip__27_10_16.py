def run_length_encode(text):
    if not text:
        return ""
    encoded = []
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

if __name__ == "__main__":
    sample_string = "aaabbcccc"
    result = run_length_encode(sample_string)
    print(result)
    empty_string = ""
    empty_result = run_length_encode(empty_string)
    print(empty_result)
    single_char = "z"
    single_result = run_length_encode(single_char)
    print(single_result)