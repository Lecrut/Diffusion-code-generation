def run_length_encode(s: str) -> str:
    if not s:
        return s
    
    result = []
    i = 0
    n = len(s)
    
    while i < n:
        current_char = s[i]
        count = 1
        j = i + 1
        while j < n and s[j] == current_char:
            count += 1
            j += 1
        
        if count > 1:
            result.append(str(count))
        
        result.append(current_char)
        i = j
    
    return "".join(result)

if __name__ == '__main__':
    samples = [
        "",
        "a",
        "aa",
        "aabcccccaaa",
        "abcdef",
        "aaaabbbccc"
    ]
    
    for sample in samples:
        encoded = run_length_encode(sample)
        print(encoded)