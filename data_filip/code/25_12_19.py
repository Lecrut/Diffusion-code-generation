def encode(data: str) -> str:
    if not data:
        return ""
    
    result = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result.append(current_char)
            result.append(str(count))
            current_char = data[i]
            count = 1
    
    result.append(current_char)
    result.append(str(count))
    
    return "".join(result)

def decode(data: str) -> str:
    if not data:
        return ""
    
    result = []
    i = 0
    
    while i < len(data):
        char = data[i]
        i += 1
        
        num_str = []
        while i < len(data) and data[i].isdigit():
            num_str.append(data[i])
            i += 1
        
        if num_str:
            count = int("".join(num_str))
            result.append(char * count)
        else:
            result.append(char)
    
    return "".join(result)

if __name__ == "__main__":
    sample_string = "AAABBBCCCCDD"
    encoded = encode(sample_string)
    decoded = decode(encoded)
    print(encoded)
    print(decoded)