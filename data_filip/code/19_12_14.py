def run_length_encode(text):
    if not text:
        return ""
    encoded = []
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                encoded.append(str(count))
            encoded.append(current_char)
            current_char = char
            count = 1
    if count > 1:
        encoded.append(str(count))
    encoded.append(current_char)
    return "".join(encoded)

def run_length_decode(encoded):
    if not encoded:
        return ""
    decoded = []
    i = 0
    n = len(encoded)
    while i < n:
        count_str = []
        while i < n and encoded[i].isdigit():
            count_str.append(encoded[i])
            i += 1
        if count_str:
            count = int("".join(count_str))
        else:
            count = 1
        if i < n:
            decoded.append(encoded[i] * count)
            i += 1
    return "".join(decoded)

if __name__ == '__main__':
    sample_text = "AAABBBCCCDDDEEEFFF"
    encoded = run_length_encode(sample_text)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)