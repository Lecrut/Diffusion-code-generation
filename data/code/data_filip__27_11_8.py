def encode_rle(text):
    if not text:
        return ""
    result = []
    count = 1
    current_char = text[0]
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = text[i]
            count = 1
    result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample_text = "aaabbccccd"
    encoded_value = encode_rle(sample_text)
    print(encoded_value)