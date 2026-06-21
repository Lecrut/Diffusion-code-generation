def encode_repeated_elements(s: str) -> str:
    if not s:
        return ""
    
    result = []
    count = 1
    length = len(s)
    
    for i in range(1, length):
        if s[i] == s[i - 1]:
            count += 1
        else:
            if count > 1:
                result.append(f"{count}{s[i-1]}")
            else:
                result.append(s[i-1])
            count = 1
    
    if count > 1:
        result.append(f"{count}{s[-1]}")
    else:
        result.append(s[-1])
        
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbc"
    encoded_result = encode_repeated_elements(sample_input)
    print(encoded_result)