def run_length_encode(text: str) -> str:
    if not text:
        return ""
    
    result = []
    count = 1
    current_char = text[0]
    
    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            if count > 1:
                result.append(f"{count}{current_char}")
            else:
                result.append(current_char)
            current_char = char
            count = 1
    
    if count > 1:
        result.append(f"{count}{current_char}")
    else:
        result.append(current_char)
        
    return "".join(result)

def run_length_decode(text: str) -> str:
    if not text:
        return ""
    
    result = []
    i = 0
    length = len(text)
    
    while i < length:
        count_str = []
        while i < length and text[i].isdigit():
            count_str.append(text[i])
            i += 1
        
        if not count_str:
            count = 1
        else:
            count = int("".join(count_str))
        
        if i < length:
            char = text[i]
            result.append(char * count)
            i += 1
    
    return "".join(result)

if __name__ == '__main__':
    original = "aaabbc"
    encoded = run_length_encode(original)
    print(encoded)
    
    decoded = run_length_decode(encoded)
    print(decoded)
    
    single = "abc"
    encoded_single = run_length_encode(single)
    print(encoded_single)
    
    empty = ""
    encoded_empty = run_length_encode(empty)
    print(encoded_empty)