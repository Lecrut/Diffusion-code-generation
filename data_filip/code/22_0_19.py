def run_length_encode(s: str) -> str:
    if not s:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(str(count) + current_char)
            current_char = char
            count = 1
    
    result.append(str(count) + current_char)
    return "".join(result)

if __name__ == "__main__":
    sample_input = "aabcccccaaa"
    encoded = run_length_encode(sample_input)
    print(encoded)
    
    sample_empty = ""
    encoded_empty = run_length_encode(sample_empty)
    print(encoded_empty)
    
    sample_single = "a"
    encoded_single = run_length_encode(sample_single)
    print(encoded_single)
    
    sample_mixed = "abcde"
    encoded_mixed = run_length_encode(sample_mixed)
    print(encoded_mixed)
    
    sample_repeated = "AAAAAABBBBBBCCCCC"
    encoded_repeated = run_length_encode(sample_repeated)
    print(encoded_repeated)