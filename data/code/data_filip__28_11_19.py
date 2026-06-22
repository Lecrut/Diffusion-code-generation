def compress_rle(s: str) -> str:
    if not s:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = s[i]
            count = 1
    
    result.append(f"{current_char}{count}")
    
    return "".join(result)

if __name__ == '__main__':
    test_cases = [
        ("", ""),
        ("A", "A1"),
        ("AA", "A2"),
        ("AABBBCCD", "A2B3C2D1"),
        ("AAAAABBBCC", "A5B3C2"),
        ("xyz", "x1y1z1")
    ]
    
    for input_val, expected in test_cases:
        result = compress_rle(input_val)
        print(result)