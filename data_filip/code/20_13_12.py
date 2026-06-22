def run_length_encode(s: str) -> list:
    if not s:
        return []
    
    encoded = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = s[i]
            count = 1
    
    encoded.append((current_char, count))
    return encoded

if __name__ == '__main__':
    sample_input = "aaabbc"
    result = run_length_encode(sample_input)
    print(result)