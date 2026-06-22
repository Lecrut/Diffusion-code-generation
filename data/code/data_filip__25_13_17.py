def run_length_encode(data: str) -> str:
    if not data:
        return ""
    
    result = []
    count = 1
    current_char = data[0]
    
    for i in range(1, len(data)):
        char = data[i]
        if char == current_char:
            count += 1
        else:
            result.append(str(count))
            result.append(current_char)
            current_char = char
            count = 1
    
    result.append(str(count))
    result.append(current_char)
    return "".join(result)

def run_length_decode(data: str) -> str:
    if not data:
        return ""
    
    result = []
    i = 0
    length = len(data)
    
    while i < length:
        count_str = []
        while i < length and data[i].isdigit():
            count_str.append(data[i])
            i += 1
        
        if i >= length:
            break
            
        count = int("".join(count_str))
        char = data[i]
        result.append(char * count)
        i += 1
    
    return "".join(result)

if __name__ == '__main__':
    encoded = run_length_encode("AAAABBBCCDAA")
    print(encoded)
    
    decoded = run_length_decode("4A3B2C1D2A")
    print(decoded)