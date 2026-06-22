def trim_whitespace(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Expected a string")
    start = 0
    end = len(text)
    
    while start < end and text[start].isspace():
        start += 1
        
    while end > start and text[end - 1].isspace():
        end -= 1
        
    return text[start:end]

if __name__ == '__main__':
    print(trim_whitespace("  hello world  "))
    print(trim_whitespace("   "))
    print(trim_whitespace("no_spaces"))