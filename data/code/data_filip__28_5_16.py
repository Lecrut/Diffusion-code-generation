def encode_rle(text):
    if not text:
        return ""
    result = []
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(str(count) + current_char)
            current_char = char
            count = 1
    result.append(str(count) + current_char)
    return "".join(result)

def decode_rle(encoded_text):
    if not encoded_text:
        return ""
    result = []
    i = 0
    while i < len(encoded_text):
        count_str = ""
        while i < len(encoded_text) and encoded_text[i].isdigit():
            count_str += encoded_text[i]
            i += 1
        if i < len(encoded_text):
            count = int(count_str)
            char = encoded_text[i]
            result.append(char * count)
            i += 1
    return "".join(result)

if __name__ == '__main__':
    original = "AAAABBBCCDAA"
    encoded = encode_rle(original)
    decoded = decode_rle(encoded)
    print(original == decoded)