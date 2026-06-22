def run_length_encode(input_string: str) -> str:
    if not input_string:
        return ""
    
    result = []
    current_char = input_string[0]
    count = 1
    
    for i in range(1, len(input_string)):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    result.append(f"{count}{current_char}")
    return "".join(result)

def run_length_decode(input_string: str) -> str:
    if not input_string:
        return ""
    
    result = []
    i = 0
    n = len(input_string)
    
    while i < n:
        count_str = []
        while i < n and input_string[i].isdigit():
            count_str.append(input_string[i])
            i += 1
        
        if not count_str:
            break
            
        count = int("".join(count_str))
        
        if i < n:
            char = input_string[i]
            result.append(char * count)
            i += 1
    
    return "".join(result)

if __name__ == '__main__':
    original = '0011100'
    encoded = run_length_encode(original)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)