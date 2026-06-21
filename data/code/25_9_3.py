def run_length_encode(s: str) -> str:
    if not s:
        return ""

    result = []
    current_char = s[0]
    count = 1
    s_len = len(s)

    for i in range(1, s_len):
        char = s[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    result.append(f"{count}{current_char}")
    
    return "".join(result)

if __name__ == '__main__':
    sample_string = "AAABBBCCCC"
    encoded = run_length_encode(sample_string)
    print(encoded)