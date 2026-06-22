def run_length_encode(text):
    if not text:
        return ""
    encoded_parts = []
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_parts.append(f"{current_char}{count}")
            current_char = char
            count = 1
    encoded_parts.append(f"{current_char}{count}")
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_text = "aaabbccccd"
    result = run_length_encode(sample_text)
    print(result)