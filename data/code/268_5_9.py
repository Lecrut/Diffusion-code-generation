def find_first_word(text):
    if not text or text.isspace():
        return ""
    
    index = 0
    while index < len(text) and text[index].isspace():
        index += 1
    
    start = index
    while index < len(text) and not text[index].isspace():
        index += 1
    
    return text[start:index]

if __name__ == '__main__':
    test_cases = [
        ("", ""),
        ("   ", ""),
        ("hello world", "hello"),
        ("  leading space", "leading"),
        ("trailing space ", "trailing"),
        ("singleword", "singleword"),
        ("multiple  spaces here", "multiple")
    ]
    
    for text, expected in test_cases:
        result = find_first_word(text)
        print(f"Input: '{text}' | Expected: '{expected}' | Result: '{result}'")