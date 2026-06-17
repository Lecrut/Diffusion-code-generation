def contains_repeated_chars(s: str) -> bool:
    s_lower = s.lower()
    return len(set(s_lower)) != len(s_lower)
if __name__ == '__main__':
    sample_strings = [
        "hello",                           
        "abcdefg",                         
        "Hello World!",                                           
        "AaBbCcDdEeFfGgHhIiJjKkLlmnnooppqqrsttuuvvwwxyz",                       
    ]
    for test_str in sample_strings:
        result = contains_repeated_chars(test_str)
        print(f"String: '{test_str}' -> Repeats found: {result}")