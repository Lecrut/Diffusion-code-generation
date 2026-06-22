def run_length_encode(s: str) -> str:
    if not s:
        return ""
    
    if len(s) == 1:
        return "1" + s
    
    result = []
    count = 1
    prev_char = s[0]
    
    for i in range(1, len(s)):
        current_char = s[i]
        if current_char == prev_char:
            count += 1
        else:
            result.append(str(count) + prev_char)
            prev_char = current_char
            count = 1
    
    result.append(str(count) + prev_char)
    
    return "".join(result)

if __name__ == '__main__':
    test_strings = [
        "",
        "A",
        "AA",
        "AAAABBBCCDAA",
        "XYZ"
    ]
    
    for s in test_strings:
        encoded = run_length_encode(s)
        print(encoded)