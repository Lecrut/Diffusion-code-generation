def encode_rle(text):
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

if __name__ == "__main__":
    sample_text = "aaabbccccd"
    encoded_value = encode_rle(sample_text)
    print(encoded_value)
    empty_text = ""
    empty_encoded = encode_rle(empty_text)
    print(empty_encoded)