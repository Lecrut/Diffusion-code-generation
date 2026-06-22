def run_length_encode(text):
    if not text:
        return ""
    result = []
    current_char = text[0]
    count = 1
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = text[i]
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbcccc"
    encoded_value = run_length_encode(sample_input)
    print(encoded_value)
    empty_input = ""
    print(run_length_encode(empty_input))
    single_input = "z"
    print(run_length_encode(single_input))