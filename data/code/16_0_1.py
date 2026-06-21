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
    sample_input = "aaabbcccc"
    result = run_length_encode(sample_input)
    print(result)
    
    empty_input = ""
    empty_result = run_length_encode(empty_input)
    print(empty_result)
    
    single_input = "z"
    single_result = run_length_encode(single_input)
    print(single_result)
    
    mixed_input = "aabbbaaa"
    mixed_result = run_length_encode(mixed_input)
    print(mixed_result)