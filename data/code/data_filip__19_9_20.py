def enhanced_rle_encode(data: str, escape_char: str = '\\', count_char: str = '#') -> str:
    if not data:
        return ""
    
    encoded = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        char = data[i]
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{count_char}{current_char}")
            current_char = char
            count = 1
    
    encoded.append(f"{count}{count_char}{current_char}")
    
    return escape_char.join(encoded)

def enhanced_rle_decode(data: str, escape_char: str = '\\', count_char: str = '#') -> str:
    if not data:
        return ""
    
    parts = data.split(escape_char)
    decoded_chars = []
    
    for part in parts:
        if not part:
            continue
        
        count_str = ""
        i = 0
        while i < len(part) and part[i] != count_char:
            count_str += part[i]
            i += 1
        
        if i < len(part) and part[i] == count_char:
            count = int(count_str)
            char = part[i + 1]
            decoded_chars.append(char * count)
        else:
            decoded_chars.append(part)
            
    return "".join(decoded_chars)

if __name__ == '__main__':
    sample_data = "AAABBBCCDDDEEE"
    encoded = enhanced_rle_encode(sample_data)
    print(encoded)
    
    sample_encoded = "10#X\\4#Y\\3#Z"
    decoded = enhanced_rle_decode(sample_encoded)
    print(decoded)