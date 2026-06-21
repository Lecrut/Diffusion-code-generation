def run_length_encode(s):
    if not s:
        return ""
    
    encoded = []
    i = 0
    n = len(s)
    
    while i < n:
        current_char = s[i]
        count = 1
        j = i + 1
        while j < n and s[j] == current_char:
            count += 1
            j += 1
        encoded.append(f"{count}{current_char}")
        i = j
    
    return "".join(encoded)

if __name__ == '__main__':
    sample_text = "aaabbbcccd"
    result = run_length_encode(sample_text)
    print(result)