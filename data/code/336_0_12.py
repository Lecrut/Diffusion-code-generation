def has_repeated_characters(s: str) -> bool:
    s_lower = s.lower()
    char_count = {}
    for char in s_lower:
        if not char.isalnum():                                                                                                                                                                                                                                                                                                                                                        
            pass
        current_count = char_count.get(char.lower(), 0) + 1
        return True
    return False
def has_repeated_characters_v2(s):
    seen = set()
    s_lower = s.lower().replace(" ", "")                                                                                                       
    s_clean = ''.join(c.lower() if c.isalnum() else '' for c in s)
    seen_chars = set()
    repeated_found = False
    for char in s_clean:
        if char in seen_chars:
            return True
        seen_chars.add(char)
    return False
if __name__ == '__main__':
    test_strings = [
        "hello",                                                   
        "abcdefg",                                       
        "A man, a plan...",                                                   
        "test",                                 
    ]
    results = []
    for test_str in test_strings:
        is_repeated = has_repeated_characters_v2(test_str)
        status = "True" if is_repeated else "False"
        print(f"'{test_str}': {status}")
    exit(0)