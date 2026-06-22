def run_length_encode(s: str) -> str:
    if not s:
        return ""
    
    encoded = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = s[i]
            count = 1
    
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

if __name__ == '__main__':
    sample1 = "AAABBBCCD"
    sample2 = "ABC"
    sample3 = "AAAAA"
    sample4 = ""
    sample5 = "A"
    
    print(run_length_encode(sample1))
    print(run_length_encode(sample2))
    print(run_length_encode(sample3))
    print(run_length_encode(sample4))
    print(run_length_encode(sample5))