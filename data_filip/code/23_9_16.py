def run_length_encode(s: str) -> str:
    if not s:
        return ""
    
    result = []
    n = len(s)
    i = 0
    
    while i < n:
        current_char = s[i]
        count = 1
        j = i + 1
        
        while j < n and s[j] == current_char:
            count += 1
            j += 1
        
        if count > 1:
            result.append(f"{count}{current_char}")
        else:
            result.append(current_char)
        
        i = j
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbccccdefghhh"
    encoded = run_length_encode(sample_input)
    print(encoded)