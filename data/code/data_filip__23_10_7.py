def encode_rle(s: str) -> list[tuple[int, str]]:
    if not s:
        return []
    
    result = []
    count = 1
    current_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append((count, current_char))
            current_char = s[i]
            count = 1
    
    result.append((count, current_char))
    return result

if __name__ == '__main__':
    sample_strings = [
        "aaabbcccc",
        "a",
        "",
        "aaaa",
        "abab",
        "1122333"
    ]
    
    for test_str in sample_strings:
        encoded = encode_rle(test_str)
        print(encoded)