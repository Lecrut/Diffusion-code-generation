def rle_encode(data):
    if not data:
        return []
    encoded = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char and count < 65535:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = char
            count = 1
    encoded.append((current_char, count))
    return encoded

def rle_decode(encoded):
    if not encoded:
        return ""
    decoded = []
    for char, count in encoded:
        decoded.append(char * count)
    return "".join(decoded)

def rle_encode_string(data):
    if not data:
        return ""
    parts = []
    for char, count in rle_encode(data):
        parts.append(f"{count}{char}")
    return "".join(parts)

def rle_decode_string(encoded):
    if not encoded:
        return ""
    decoded = []
    i = 0
    while i < len(encoded):
        num_str = ""
        while i < len(encoded) and encoded[i].isdigit():
            num_str += encoded[i]
            i += 1
        if i < len(encoded):
            count = int(num_str) if num_str else 1
            char = encoded[i]
            i += 1
            decoded.append(char * count)
    return "".join(decoded)

if __name__ == '__main__':
    sample_data = "AAABBBCCCDAA"
    encoded = rle_encode(sample_data)
    decoded = rle_decode(encoded)
    print(f"Original: {sample_data}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")
    
    sample_string = "HHHHlllooooo"
    encoded_str = rle_encode_string(sample_string)
    decoded_str = rle_decode_string(encoded_str)
    print(f"Original String: {sample_string}")
    print(f"Encoded String: {encoded_str}")
    print(f"Decoded String: {decoded_str}")