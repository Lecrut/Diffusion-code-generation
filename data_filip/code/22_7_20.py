def decode_rle(encoded: str) -> str:
    if not encoded:
        return ""
    
    decoded_parts = []
    i = 0
    n = len(encoded)
    
    while i < n:
        count_str = ""
        while i < n and encoded[i].isdigit():
            count_str += encoded[i]
            i += 1
        
        if count_str:
            count = int(count_str)
        else:
            count = 1
        
        if i < n:
            char = encoded[i]
            decoded_parts.append(char * count)
            i += 1
    
    return "".join(decoded_parts)

if __name__ == '__main__':
    sample_encoded_1 = "2a3b4c"
    result_1 = decode_rle(sample_encoded_1)
    print(result_1)
    
    sample_encoded_2 = "12w3b24a"
    result_2 = decode_rle(sample_encoded_2)
    print(result_2)
    
    sample_encoded_3 = ""
    result_3 = decode_rle(sample_encoded_3)
    print(result_3)
    
    sample_encoded_4 = "a"
    result_4 = decode_rle(sample_encoded_4)
    print(result_4)
    
    sample_encoded_5 = "100z"
    result_5 = decode_rle(sample_encoded_5)
    print(result_5)