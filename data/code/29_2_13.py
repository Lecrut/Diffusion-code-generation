def run_length_encode(s):
    if not s:
        return ""
    
    encoded = []
    current_char = s[0]
    count = 1
    
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                encoded.append(f"{count}{current_char}")
            else:
                encoded.append(current_char)
            current_char = char
            count = 1
    
    if count > 1:
        encoded.append(f"{count}{current_char}")
    else:
        encoded.append(current_char)
    
    return "".join(encoded)

if __name__ == "__main__":
    test_cases = [
        "aaabbc",
        "abc",
        "aabb",
        "aaaa",
        "abba",
        "",
        "a",
        "zzzzyyyyxxww",
    ]
    
    for test in test_cases:
        result = run_length_encode(test)
        print(f"{test!r} -> {result!r}")