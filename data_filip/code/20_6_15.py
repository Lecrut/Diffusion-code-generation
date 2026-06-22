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
            if count > 1:
                encoded.append(str(count))
            encoded.append(current_char)
            current_char = s[i]
            count = 1
    
    if count > 1:
        encoded.append(str(count))
    encoded.append(current_char)
    
    return "".join(encoded)

if __name__ == '__main__':
    sample = "AAABBBCCD"
    print(run_length_encode(sample))
    
    sample_empty = ""
    print(run_length_encode(sample_empty))
    
    sample_single = "A"
    print(run_length_encode(sample_single))
    
    sample_mixed = "ABC"
    print(run_length_encode(sample_mixed))
    
    sample_repeated = "AAAABBBCCDAA"
    print(run_length_encode(sample_repeated))