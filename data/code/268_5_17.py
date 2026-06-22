MAX_ITERATIONS = 100

def find_first_word(text):
    if not text:
        return ""
    
    index = 0
    while index < len(text) and text[index].isspace():
        index += 1
    
    if index == len(text):
        return ""
    
    first_word_start = index
    while index < len(text) and not text[index].isspace():
        index += 1
    
    return text[first_word_start:index]

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