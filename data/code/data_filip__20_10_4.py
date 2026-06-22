def run_length_encode(s: str) -> str:
    if not s:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        char = s[i]
        if char == current_char:
            count += 1
        else:
            result.append(str(count))
            result.append(current_char)
            current_char = char
            count = 1
    
    result.append(str(count))
    result.append(current_char)
    
    return "".join(result)

if __name__ == '__main__':
    test_string = "aabcccccaaa"
    encoded = run_length_encode(test_string)
    print(encoded)
    
    test_string_2 = "abc"
    encoded_2 = run_length_encode(test_string_2)
    print(encoded_2)
    
    test_string_3 = ""
    encoded_3 = run_length_encode(test_string_3)
    print(encoded_3)