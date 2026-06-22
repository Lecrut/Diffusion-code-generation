def encode_compressed(text):
    if not text:
        return text
    encoded_parts = []
    last_char = text[0]
    current_run = 1
    char_count = len(text)
    index = 1
    while index < char_count:
        char = text[index]
        if char == last_char:
            current_run += 1
        else:
            encoded_parts.append(str(current_run))
            encoded_parts.append(last_char)
            last_char = char
            current_run = 1
        index += 1
    encoded_parts.append(str(current_run))
    encoded_parts.append(last_char)
    return "".join(encoded_parts)

def decode_compressed(compressed_text):
    if not compressed_text:
        return ""
    decoded_chars = []
    index = 0
    text_len = len(compressed_text)
    while index < text_len:
        count_str = []
        while index < text_len and compressed_text[index].isdigit():
            count_str.append(compressed_text[index])
            index += 1
        count = int("".join(count_str))
        if index < text_len:
            char = compressed_text[index]
            decoded_chars.append(char * count)
            index += 1
    return "".join(decoded_chars)

if __name__ == '__main__':
    source = "AAAABBBCCDA"
    compressed = encode_compressed(source)
    original = decode_compressed(compressed)
    print(compressed)
    print(original)