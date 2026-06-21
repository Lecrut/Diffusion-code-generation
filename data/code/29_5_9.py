def encode_run_length(s: str) -> str:
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

if __name__ == '__main__':
    test_strings = ["AABBC", "", "Z", "WWWWWWWWWW"]
    for s in test_strings:
        encoded = encode_run_length(s)
        print(encoded)