def run_length_encode(text):
    if not text:
        return ""
    
    result = []
    current_char = text[0]
    count = 1
    
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                result.append(f"{count}{current_char}")
            else:
                result.append(current_char)
            current_char = char
            count = 1
    
    if count > 1:
        result.append(f"{count}{current_char}")
    else:
        result.append(current_char)
    
    return "".join(result)

def run_length_decode(text):
    if not text:
        return ""
    
    result = []
    current_num_str = []
    
    for char in text:
        if char.isdigit():
            current_num_str.append(char)
        else:
            if current_num_str:
                count = int("".join(current_num_str))
                result.append(char * count)
                current_num_str = []
            else:
                result.append(char)
    
    if current_num_str:
        count = int("".join(current_num_str))
        result.append(current_num_str[0] if len(current_num_str) == 1 else "")
    
    return "".join(result)

if __name__ == '__main__':
    original = "aaabbbcccaaa"
    encoded = run_length_encode(original)
    decoded = run_length_decode(encoded)
    print(f"{original} -> {encoded} -> {decoded}")
    
    test_cases = [
        ("", ""),
        ("a", "a"),
        ("aaa", "3a"),
        ("aabbbcccc", "2a3b4c"),
        ("abc", "abc")
    ]
    
    for original, expected in test_cases:
        enc = run_length_encode(original)
        dec = run_length_decode(enc)
        print(f"Input: '{original}' | Encoded: '{enc}' | Decoded: '{dec}' | Match: {dec == original}")
        
    large_string = "a" * 1000000 + "b" * 500000
    encoded_large = run_length_encode(large_string)
    decoded_large = run_length_decode(encoded_large)
    print(f"Large string encoded length: {len(encoded_large)}")
    print(f"Large string decoded matches original: {decoded_large == large_string}")