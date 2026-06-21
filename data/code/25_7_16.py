def rle_encode(text):
    if not text:
        return ""
    encoded = []
    count = 1
    current_char = text[0]
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            encoded.append(current_char)
            if count > 1:
                encoded.append(str(count))
            current_char = text[i]
            count = 1
    encoded.append(current_char)
    if count > 1:
        encoded.append(str(count))
    return "".join(encoded)

def is_compression_effective(original_string):
    encoded_string = rle_encode(original_string)
    return len(encoded_string) < len(original_string)

if __name__ == '__main__':
    sample_text = "aaaabbbcc"
    result = is_compression_effective(sample_text)
    print(result)