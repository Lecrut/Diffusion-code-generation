def encode_rle(text):
    if not text:
        return ""
    result = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result.append(f"{count}{text[i - 1]}")
            count = 1
    result.append(f"{count}{text[-1]}")
    return "".join(result)

def decode_rle(encoded):
    if not encoded:
        return ""
    result = []
    i = 0
    while i < len(encoded):
        count_str = ""
        while i < len(encoded) and encoded[i].isdigit():
            count_str += encoded[i]
            i += 1
        char = encoded[i]
        i += 1
        result.append(char * int(count_str))
    return "".join(result)

if __name__ == '__main__':
    original_text = "AAAABBBCCDAA"
    encoded_result = encode_rle(original_text)
    print(encoded_result)
    decoded_result = decode_rle(encoded_result)
    print(decoded_result)