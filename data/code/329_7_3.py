def safe_string_equality(a, b):
    if isinstance(a, str) and isinstance(b, str):
        return a == b
    return False
if __name__ == '__main__':
    print(safe_string_equality("hello", "hello"))
    print(safe_string_equality("hello", "world"))
    print(safe_string_equality("hello", 123))
    print(safe_string_equality(None, "hello"))
    print(safe_string_equality("", ""))
    print(safe_string_equality(123, 456))