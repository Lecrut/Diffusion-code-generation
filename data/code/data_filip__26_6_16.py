def run_length_encode(text):
    if not text:
        return ""
    encoded_parts = []
    current_char = text[0]
    count = 1
    for index in range(1, len(text)):
        if text[index] == current_char:
            count += 1
        else:
            encoded_parts.append(str(count) + current_char)
            current_char = text[index]
            count = 1
    encoded_parts.append(str(count) + current_char)
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_text = "aaabbccccdd"
    result = run_length_encode(sample_text)
    print(result)