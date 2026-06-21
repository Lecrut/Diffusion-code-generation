def decode_rle(encoded: str) -> str:
    if not encoded:
        return ""
    
    result = []
    i = 0
    length = len(encoded)
    
    while i < length:
        char = encoded[i]
        i += 1
        
        if not char.isdigit():
            result.append(char)
            continue
        
        count_str = ""
        while i < length and encoded[i].isdigit():
            count_str += encoded[i]
            i += 1
        
        if not count_str:
            raise ValueError(f"Invalid RLE format: digit '{char}' followed by no count at position {i-1}")
        
        count = int(count_str)
        if count < 1:
            raise ValueError(f"Invalid count: {count} for character '{char}'")
        
        result.append(char * count)
    
    return "".join(result)

if __name__ == '__main__':
    sample_encoded = "2A3B1C"
    decoded_value = decode_rle(sample_encoded)
    print(decoded_value)