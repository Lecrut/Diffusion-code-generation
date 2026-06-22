def encode_rle(data: str) -> str:
    if not data:
        return ""
    
    encoded_parts = []
    count = 1
    length = len(data)
    
    for i in range(length):
        if i + 1 < length and data[i] == data[i + 1]:
            count += 1
        else:
            encoded_parts.append(str(count) + data[i])
            count = 1
            
    return "".join(encoded_parts)

def decode_rle(encoded: str) -> str:
    if not encoded:
        return ""
    
    decoded_parts = []
    i = 0
    length = len(encoded)
    
    while i < length:
        digit_start = i
        while i < length and encoded[i].isdigit():
            i += 1
            
        count = int(encoded[digit_start:i])
        decoded_parts.append(encoded[i] * count)
        i += 1
        
    return "".join(decoded_parts)

if __name__ == '__main__':
    sample_input = "AAABBBCCCCDDDEEE"
    encoded_result = encode_rle(sample_input)
    decoded_result = decode_rle(encoded_result)
    
    print(f"Original: {sample_input}")
    print(f"Encoded: {encoded_result}")
    print(f"Decoded: {decoded_result}")
    print(f"Round-trip successful: {sample_input == decoded_result}")