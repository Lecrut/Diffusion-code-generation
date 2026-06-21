def encode_rle(data: str) -> str:
    if not data:
        return ""
    
    result = []
    current_char = data[0]
    count = 1
    length = len(data)
    
    for i in range(1, length):
        char = data[i]
        if char == current_char:
            count += 1
        else:
            result.append(str(count) + current_char)
            current_char = char
            count = 1
    
    result.append(str(count) + current_char)
    
    return "".join(result)

def decode_rle(data: str) -> str:
    if not data:
        return ""
    
    result = []
    i = 0
    length = len(data)
    
    while i < length:
        num_str = []
        while i < length and data[i].isdigit():
            num_str.append(data[i])
            i += 1
        
        if not num_str:
            break
            
        count = int("".join(num_str))
        
        if i < length:
            char = data[i]
            i += 1
            result.append(char * count)
        else:
            break
    
    return "".join(result)

if __name__ == '__main__':
    original = "AAAABBBCCDAA"
    encoded = encode_rle(original)
    print(encoded)
    
    decoded = decode_rle(encoded)
    print(decoded)