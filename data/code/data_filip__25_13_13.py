def run_length_encode(text: str) -> str:
    if not text:
        return ""
    
    result = []
    current_char = text[0]
    count = 1
    
    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    result.append(f"{count}{current_char}")
    
    return "".join(result)

def run_length_decode(encoded_text: str) -> str:
    if not encoded_text:
        return ""
    
    result = []
    i = 0
    n = len(encoded_text)
    
    while i < n:
        count_str = []
        while i < n and encoded_text[i].isdigit():
            count_str.append(encoded_text[i])
            i += 1
        
        if not count_str:
            raise ValueError("Invalid encoded string: expected a digit at start or after previous segment.")
        
        count = int("".join(count_str))
        
        if i >= n:
            raise ValueError("Invalid encoded string: missing character after count.")
        
        char = encoded_text[i]
        i += 1
        
        result.append(char * count)
    
    return "".join(result)

if __name__ == '__main__':
    original_string = "aaabbbbcccd"
    encoded = run_length_encode(original_string)
    decoded = run_length_decode(encoded)
    
    print(encoded)
    print(decoded)
    print(original_string == decoded)