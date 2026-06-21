def run_length_encode(text):
    if not text:
        return ""
    result = []
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1
    result.append(f"{current_char}{count}")
    return " ".join(result)

if __name__ == '__main__':
    sample_text = "aaabbccccd"
    encoded_text = run_length_encode(sample_text)
    print(encoded_text)
    single_char_text = "z"
    print(run_length_encode(single_char_text))
    empty_text = ""
    print(run_length_encode(empty_text))
    mixed_text = "111223333"
    print(run_length_encode(mixed_text))