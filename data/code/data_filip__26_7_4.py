def run_length_encode(s: str) -> str:
    if not s:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = s[i]
            count = 1
    
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    sample = "AAABBBCCD"
    print(run_length_encode(sample))
    
    sample2 = "XYZ"
    print(run_length_encode(sample2))
    
    sample3 = ""
    print(run_length_encode(sample3))
    
    sample4 = "A"
    print(run_length_encode(sample4))
    
    sample5 = "AAABBBCCCDDD"
    print(run_length_encode(sample5))