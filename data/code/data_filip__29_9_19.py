def encode_repeated_elements(s: str) -> str:
    if not s:
        return ""
    
    result = []
    i = 0
    n = len(s)
    
    while i < n:
        current_char = s[i]
        count = 0
        while i < n and s[i] == current_char:
            count += 1
            i += 1
        
        if count > 1:
            result.append(f"{count}{current_char}")
        else:
            result.append(current_char)
    
    return "".join(result)

if __name__ == '__main__':
    test_string = "aaabbc"
    encoded = encode_repeated_elements(test_string)
    print(encoded)