def enhanced_rle_encode(data: str) -> str:
    if not data:
        return ""
    
    result = []
    i = 0
    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            count += 1
            i += 1
        result.append(f"{count}{data[i]}")
        i += 1
    return "".join(result)

def enhanced_rle_decode(data: str) -> str:
    if not data:
        return ""
    
    result = []
    i = 0
    while i < len(data):
        count_str = ""
        while i < len(data) and data[i].isdigit():
            count_str += data[i]
            i += 1
        count = int(count_str) if count_str else 0
        if i < len(data):
            result.append(data[i] * count)
            i += 1
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AABBBCCCCDD"
    encoded = enhanced_rle_encode(sample_input)
    print(encoded)
    decoded = enhanced_rle_decode(encoded)
    print(decoded)
    test_with_escapes = "AA!!BB@@CC##DD"
    encoded_escapes = enhanced_rle_encode(test_with_escapes)
    print(encoded_escapes)
    decoded_escapes = enhanced_rle_decode(encoded_escapes)
    print(decoded_escapes)