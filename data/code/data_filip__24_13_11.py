def encode_rle(data: str) -> str:
    if not data:
        return ""
    encoded_parts = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_parts.append(f"{count}{current_char}")
            current_char = char
            count = 1
    encoded_parts.append(f"{count}{current_char}")
    return "".join(encoded_parts)

def decode_rle(encoded: str) -> str:
    decoded_parts = []
    i = 0
    while i < len(encoded):
        if not encoded[i].isdigit():
            raise ValueError(f"Invalid RLE format at index {i}: expected digit")
        j = i
        while j < len(encoded) and encoded[j].isdigit():
            j += 1
        count = int(encoded[i:j])
        if j >= len(encoded):
            raise ValueError("Invalid RLE format: missing character after count")
        char = encoded[j]
        decoded_parts.append(char * count)
        i = j + 1
    return "".join(decoded_parts)

if __name__ == '__main__':
    sample_data = "AAAABBBCCDAA"
    encoded = encode_rle(sample_data)
    print(encoded)
    decoded = decode_rle(encoded)
    print(decoded)
    assert decoded == sample_data, "Encoding/Decoding mismatch"
    empty_encoded = encode_rle("")
    print(empty_encoded)
    single_encoded = encode_rle("A")
    print(single_encoded)
    single_decoded = decode_rle(single_encoded)
    print(single_decoded)
    complex_encoded = encode_rle("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW")
    print(complex_encoded)
    complex_decoded = decode_rle(complex_encoded)
    print(complex_decoded)
    assert complex_decoded == "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW", "Complex test failed"