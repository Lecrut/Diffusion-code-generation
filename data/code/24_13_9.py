def encode_rle(data: str) -> str:
    if not data:
        return ""
    result = []
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result.append(str(count) + current_char)
            current_char = data[i]
            count = 1
    result.append(str(count) + current_char)
    return "".join(result)

def decode_rle(encoded: str) -> str:
    if not encoded:
        return ""
    result = []
    i = 0
    while i < len(encoded):
        count_str = []
        while i < len(encoded) and encoded[i].isdigit():
            count_str.append(encoded[i])
            i += 1
        if not count_str:
            return ""
        count = int("".join(count_str))
        if i >= len(encoded):
            return ""
        char = encoded[i]
        i += 1
        result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    sample_data = "AAABBBCCD"
    encoded = encode_rle(sample_data)
    print(encoded)
    decoded = decode_rle(encoded)
    print(decoded)
    assert decoded == sample_data
    complex_sample = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    encoded_complex = encode_rle(complex_sample)
    print(encoded_complex)
    decoded_complex = decode_rle(encoded_complex)
    print(decoded_complex)
    assert decoded_complex == complex_sample
    empty_sample = ""
    encoded_empty = encode_rle(empty_sample)
    print(encoded_empty)
    decoded_empty = decode_rle(encoded_empty)
    print(decoded_empty)
    assert decoded_empty == empty_sample