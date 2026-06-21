def run_length_encode(s):
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
    sample_input = "AAABBBCCCD"
    encoded = run_length_encode(sample_input)
    print(encoded)
    
    empty_input = ""
    encoded_empty = run_length_encode(empty_input)
    print(encoded_empty)
    
    single_char = "A"
    encoded_single = run_length_encode(single_char)
    print(encoded_single)
    
    mixed_input = "XYZZZZZ"
    encoded_mixed = run_length_encode(mixed_input)
    print(encoded_mixed)