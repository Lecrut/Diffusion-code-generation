def encode(data: str) -> str:
    if not data:
        return ""
    
    result = []
    count = 1
    current_char = data[0]
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = data[i]
            count = 1
    
    result.append(f"{count}{current_char}")
    
    return "".join(result)

def decode(data: str) -> str:
    if not data:
        return ""
    
    result = []
    i = 0
    
    while i < len(data):
        count_str = ""
        while i < len(data) and data[i].isdigit():
            count_str += data[i]
            i += 1
        
        if i < len(data):
            count = int(count_str)
            char = data[i]
            result.append(char * count)
            i += 1
    
    return "".join(result)

if __name__ == '__main__':
    original_string = "AAAABBBCCDAA"
    
    encoded_value = encode(original_string)
    print(encoded_value)
    
    decoded_value = decode(encoded_value)
    print(decoded_value)