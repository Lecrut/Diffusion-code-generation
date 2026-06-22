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
    print(run_length_encode("AAAABBBCCDAA"))
    print(run_length_encode(""))
    print(run_length_encode("Z"))
    print(run_length_encode("aabbbcccc"))