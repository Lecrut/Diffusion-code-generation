def decompress_rle(encoded: str) -> str:
    if not encoded:
        return ""
    
    result = []
    i = 0
    n = len(encoded)
    
    while i < n:
        count_str = ""
        while i < n and encoded[i].isdigit():
            count_str += encoded[i]
            i += 1
        
        if count_str:
            count = int(count_str)
        else:
            count = 1
        
        if i < n:
            char = encoded[i]
            result.append(char * count)
            i += 1
        else:
            break
    
    return "".join(result)

if __name__ == '__main__':
    test_cases = [
        ("3a2b", "aaabb"),
        ("10z", "zzzzzzzzzz"),
        ("a2b", "abb"),
        ("", ""),
        ("1x2y3z", "xyyyzzz"),
        ("5A", "AAAAA"),
        ("2a3B4c", "aaBBBcccc"),
    ]
    
    for encoded, expected in test_cases:
        result = decompress_rle(encoded)
        print(result)