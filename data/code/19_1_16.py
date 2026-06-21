def decode_rle(encoded: str) -> str:
    if not encoded:
        return ""
    
    result = []
    i = 0
    n = len(encoded)
    
    while i < n:
        if encoded[i].isdigit():
            j = i
            while j < n and encoded[j].isdigit():
                j += 1
            count_str = encoded[i:j]
            if j >= n:
                raise ValueError("Invalid RLE format: digit at end without character")
            char = encoded[j]
            result.append(char * int(count_str))
            i = j + 1
        else:
            raise ValueError("Invalid RLE format: expected digit")
    
    return "".join(result)

if __name__ == '__main__':
    sample_encoded = "3a2b5c"
    decoded_value = decode_rle(sample_encoded)
    print(decoded_value)