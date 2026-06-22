MAX_READ = 1024

def find_first_word(text):
    if not text:
        return ""
    
    i = 0
    while i < len(text) and text[i].isspace():
        i += 1
    
    if i == len(text):
        return ""
    
    j = i + 1
    while j < len(text) and not text[j].isspace():
        j += 1
    
    return text[i:j]

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