def rle_encode_limited(data, max_run):
    if not data:
        return []
    if max_run < 1:
        raise ValueError("max_run must be positive")
    
    encoded = []
    i = 0
    length = len(data)
    
    while i < length:
        char = data[i]
        count = 0
        while i < length and count < max_run and data[i] == char:
            count += 1
            i += 1
        encoded.append((char, count))
    
    return encoded

def rle_decode_limited(encoded_pairs):
    if not encoded_pairs:
        return ""
    
    result = []
    for char, count in encoded_pairs:
        result.append(char * count)
    
    return "".join(result)

if __name__ == "__main__":
    test_data = "AAAAAAAAABBBBBBCCDD"
    limit = 3
    
    encoded = rle_encode_limited(test_data, limit)
    decoded = rle_decode_limited(encoded)
    
    print(encoded)
    print(decoded)
    print(test_data == decoded)