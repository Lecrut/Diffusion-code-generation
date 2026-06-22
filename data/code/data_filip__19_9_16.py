def enhance_rle_encode(text: str) -> str:
    if not text:
        return ""
    result = []
    count = 1
    prev_char = text[0]
    for i in range(1, len(text)):
        current_char = text[i]
        if current_char == prev_char:
            count += 1
        else:
            if prev_char in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                result.append('\\')
                result.append(prev_char)
            else:
                result.append(prev_char)
            if count > 1:
                result.append(str(count))
            prev_char = current_char
            count = 1
    if prev_char in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        result.append('\\')
        result.append(prev_char)
    else:
        result.append(prev_char)
    if count > 1:
        result.append(str(count))
    return "".join(result)

def enhance_rle_decode(encoded_text: str) -> str:
    if not encoded_text:
        return ""
    result = []
    i = 0
    while i < len(encoded_text):
        char = encoded_text[i]
        if char == '\\' and i + 1 < len(encoded_text) and encoded_text[i + 1] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            result.append(encoded_text[i + 1])
            i += 2
            continue
        if i + 1 < len(encoded_text) and encoded_text[i + 1] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            count_str = encoded_text[i + 1]
            count = int(count_str)
            result.append(char * count)
            i += 2
        else:
            result.append(char)
            i += 1
    return "".join(result)

if __name__ == '__main__':
    original = "AA11BBB"
    encoded = enhance_rle_encode(original)
    decoded = enhance_rle_decode(encoded)
    print(encoded)
    print(decoded)
    print(original == decoded)