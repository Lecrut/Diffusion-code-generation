def rle_encode(text):
    if not text:
        return ""
    result = []
    count = 1
    current_char = text[0]
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(str(count) + current_char)
            current_char = char
            count = 1
    result.append(str(count) + current_char)
    return "".join(result)

def rle_decode(text):
    if not text:
        return ""
    result = []
    num_str = []
    for char in text:
        if char.isdigit():
            num_str.append(char)
        else:
            count = int("".join(num_str))
            result.append(char * count)
            num_str = []
    return "".join(result)

if __name__ == '__main__':
    sample_text = "AAAABBBCCDAA"
    encoded = rle_encode(sample_text)
    print(encoded)
    decoded = rle_decode(encoded)
    print(decoded)