def strip_whitespace(s: str) -> str:
    return s.strip()

if __name__ == '__main__':
    result = strip_whitespace("  hello world  ")
    print(repr(result))
    
    result2 = strip_whitespace("  ")
    print(repr(result2))
    
    result3 = strip_whitespace("")
    print(repr(result3))