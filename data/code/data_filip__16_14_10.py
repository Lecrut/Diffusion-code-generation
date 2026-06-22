def encode_rle(text: str) -> str:
    if not text:
        return ""
    
    encoded = []
    current_char = text[0]
    count = 1
    
    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

def decode_rle(encoded_text: str) -> str:
    if not encoded_text:
        return ""
    
    decoded = []
    i = 0
    n = len(encoded_text)
    
    while i < n:
        count_str = ""
        while i < n and encoded_text[i].isdigit():
            count_str += encoded_text[i]
            i += 1
        
        if i < n:
            char = encoded_text[i]
            count = int(count_str)
            decoded.append(char * count)
            i += 1
    
    return "".join(decoded)

if __name__ == '__main__':
    original = "AAAAAAAAAABBBCCDDDEEE"
    encoded = encode_rle(original)
    print(encoded)
    
    decoded = decode_rle(encoded)
    print(decoded)
    
    empty = ""
    empty_encoded = encode_rle(empty)
    print(empty_encoded)
    
    single = "A"
    single_encoded = encode_rle(single)
    single_decoded = decode_rle(single_encoded)
    print(single_decoded)