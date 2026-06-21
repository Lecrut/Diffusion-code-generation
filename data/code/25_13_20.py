def run_length_encode(data: str) -> str:
    if not data:
        return ""
    
    result = []
    n = len(data)
    i = 0
    
    while i < n:
        current_char = data[i]
        count = 1
        i += 1
        
        while i < n and data[i] == current_char:
            count += 1
            i += 1
        
        result.append(f"{current_char}{count}")
    
    return "".join(result)

def run_length_decode(encoded_data: str) -> str:
    if not encoded_data:
        return ""
    
    result = []
    i = 0
    n = len(encoded_data)
    
    while i < n:
        char = encoded_data[i]
        i += 1
        
        if i >= n:
            break
            
        count_str = []
        while i < n and encoded_data[i].isdigit():
            count_str.append(encoded_data[i])
            i += 1
        
        if count_str:
            count = int("".join(count_str))
            result.append(char * count)
        else:
            result.append(char)
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAABBBCCCCDDDDD"
    encoded = run_length_encode(sample_input)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)