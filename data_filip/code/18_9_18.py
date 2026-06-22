def run_length_encode(s: str) -> str:
    if not s:
        return ""
    
    result = []
    count = 1
    current_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(str(count))
            result.append(current_char)
            current_char = s[i]
            count = 1
    
    result.append(str(count))
    result.append(current_char)
    
    return "".join(result)

if __name__ == '__main__':
    sample_string = "AAABBBCCDAA"
    encoded = run_length_encode(sample_string)
    print(encoded)
    
    sample_empty = ""
    encoded_empty = run_length_encode(sample_empty)
    print(encoded_empty)
    
    sample_single = "A"
    encoded_single = run_length_encode(sample_single)
    print(encoded_single)
    
    sample_mixed = "aabbbc"
    encoded_mixed = run_length_encode(sample_mixed)
    print(encoded_mixed)