def encode_rle(text):
    if not text:
        return ""
    result = []
    count = 1
    for index in range(len(text)):
        current_char = text[index]
        if index + 1 < len(text) and current_char == text[index + 1]:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            count = 1
    return "".join(result)

if __name__ == '__main__':
    sample_text = "aaabbccccd"
    encoded_result = encode_rle(sample_text)
    print(encoded_result)