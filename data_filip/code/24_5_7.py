def rle_encode(data):
    if not data:
        return ""
    
    encoded = []
    current_char = data[0]
    count = 1
    
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

def rle_decode(encoded):
    if not encoded:
        return ""
    
    decoded = []
    i = 0
    while i < len(encoded):
        if not encoded[i].isdigit():
            raise ValueError(f"Invalid RLE format: expected digit at index {i}")
        
        num_str = ""
        while i < len(encoded) and encoded[i].isdigit():
            num_str += encoded[i]
            i += 1
        
        if i >= len(encoded):
            raise ValueError("Invalid RLE format: expected character after count")
        
        count = int(num_str)
        char = encoded[i]
        decoded.append(char * count)
        i += 1
    
    return "".join(decoded)

if __name__ == '__main__':
    sample_string = "AAABBBCCD"
    encoded = rle_encode(sample_string)
    print(encoded)
    
    decoded = rle_decode(encoded)
    print(decoded)
    
    empty_string = ""
    encoded_empty = rle_encode(empty_string)
    print(encoded_empty)
    
    decoded_empty = rle_decode(encoded_empty)
    print(decoded_empty)
    
    single_char = "Z"
    encoded_single = rle_encode(single_char)
    print(encoded_single)
    
    decoded_single = rle_decode(encoded_single)
    print(decoded_single)
    
    complex_string = "ABC"
    encoded_complex = rle_encode(complex_string)
    print(encoded_complex)
    
    decoded_complex = rle_decode(encoded_complex)
    print(decoded_complex)