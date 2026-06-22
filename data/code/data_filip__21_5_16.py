def run_length_encode(s: str) -> list[tuple[str, int]]:
    if not s:
        return []
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = s[i]
            count = 1
    
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    sample_string = "aaabbcddd"
    encoded = run_length_encode(sample_string)
    print(encoded)
    
    sample_string_empty = ""
    encoded_empty = run_length_encode(sample_string_empty)
    print(encoded_empty)
    
    sample_string_single = "z"
    encoded_single = run_length_encode(sample_string_single)
    print(encoded_single)
    
    sample_string_mixed = "aabbbcccc"
    encoded_mixed = run_length_encode(sample_string_mixed)
    print(encoded_mixed)