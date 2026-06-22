def encode_run_length(text):
    if not text:
        return ""
    encoded_parts = []
    count = 1
    shifted = text[1:] + '\x00'
    for char, next_char in zip(text, shifted):
        if char == next_char:
            count += 1
        else:
            encoded_parts.append(char)
            if count > 1:
                encoded_parts.append(str(count))
            count = 1
    return "".join(encoded_parts)

if __name__ == '__main__':
    input_text = 'AAAAABBBB'
    print(encode_run_length(input_text))