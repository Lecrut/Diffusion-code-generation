def run_length_encode(input_string: str) -> str:
    if not input_string:
        return ""
    
    encoded_chars = []
    current_char = input_string[0]
    current_count = 1
    
    for char in input_string[1:]:
        if char == current_char:
            current_count += 1
        else:
            encoded_chars.append(f"{current_count}{current_char}")
            current_char = char
            current_count = 1
    
    encoded_chars.append(f"{current_count}{current_char}")
    return "".join(encoded_chars)

if __name__ == '__main__':
    test_string = "AAABBBCCDAA"
    result = run_length_encode(test_string)
    print(result)