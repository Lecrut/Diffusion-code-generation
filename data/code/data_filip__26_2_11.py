def run_length_encode(s: str) -> list[tuple[str, int]]:
    if not s:
        return []
    
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

if __name__ == '__main__':
    test_strings = [
        "",
        "a",
        "aaabbbcccc",
        "abc",
        "aaaabbbbaa"
    ]
    
    for s in test_strings:
        encoded = run_length_encode(s)
        print(f"run_length_encode({s!r}) = {encoded}")