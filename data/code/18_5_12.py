def run_length_encode(s: str) -> list:
    if not s:
        return []
    if len(s) == 1:
        return [(s, 1)]
    
    result = []
    current_char = s[0]
    count = 1
    
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    
    result.append((current_char, count))
    return result

def run_length_encode_fast(s: str) -> list:
    if not s:
        return []
    
    result = []
    prev = s[0]
    count = 1
    
    for char in s[1:]:
        if char == prev:
            count += 1
        else:
            result.append((prev, count))
            prev = char
            count = 1
    result.append((prev, count))
    return result

if __name__ == '__main__':
    test_cases = ["", "a", "aa", "aaa", "aabbc", "wwwwaaadexxxxxx"]
    for test in test_cases:
        encoded = run_length_encode_fast(test)
        print(f"Input: '{test}' -> Output: {encoded}")