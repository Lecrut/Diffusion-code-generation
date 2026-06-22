import re

def rle_encode(data):
    if not data:
        return ""
    encoded = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char and count < 9:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = char
            count = 1
    encoded.append(str(count) + current_char)
    return "".join(encoded)

def rle_decode(encoded):
    if not encoded:
        return ""
    decoded = []
    i = 0
    while i < len(encoded):
        count = int(encoded[i])
        i += 1
        if i < len(encoded):
            char = encoded[i]
            decoded.append(char * count)
            i += 1
    return "".join(decoded)

def bidirectional_rle_process(text):
    compressed = rle_encode(text)
    decompressed = rle_decode(compressed)
    integrity_ok = (text == decompressed)
    return compressed, decompressed, integrity_ok

if __name__ == '__main__':
    sample_text = "AAABBBCCCCDDEEEEE"
    result = bidirectional_rle_process(sample_text)
    print(result)