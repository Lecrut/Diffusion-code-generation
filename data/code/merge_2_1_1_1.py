def check_uppercase(s: str) -> bool:
    return any(c.isupper() for c in s)
if __name__ == '__main__':
    test_cases = [
        "hello",
        "Hello",
        "HELLO WORLD",
        "",
        "123"
    ]
    print("Testing uppercase check:")
    for text in test_cases:
        result = check_uppercase(text)
        print(f"'{text}' -> {result}")