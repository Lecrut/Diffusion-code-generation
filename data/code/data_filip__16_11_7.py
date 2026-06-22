def run_length_encode(s: str) -> str:
    if not s:
        return ""
    
    encoded = []
    count = 1
    current_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append(str(count))
            encoded.append(current_char)
            current_char = s[i]
            count = 1
    
    encoded.append(str(count))
    encoded.append(current_char)
    
    return "".join(encoded)

if __name__ == '__main__':
    sample_string = "aaabbc"
    result = run_length_encode(sample_string)
    print(result)