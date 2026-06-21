def run_length_encoding(s: str) -> str:
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
        result.append(f"{count}{current_char}")
        i = j
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbcdddd"
    encoded_result = run_length_encoding(sample_input)
    print(encoded_result)
    
    sample_empty = ""
    print(run_length_encoding(sample_empty))
    
    sample_single = "a"
    print(run_length_encoding(sample_single))
    
    sample_mixed = "aabbccccdddeef"
    print(run_length_encoding(sample_mixed))