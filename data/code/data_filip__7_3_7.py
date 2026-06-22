def has_special_chars(s: str) -> bool:
    return any(not c.isalnum() and not c.isspace() for c in s)

if __name__ == '__main__':
    sample1 = "HelloWorld"
    sample2 = "Hello@World"
    sample3 = "Test 123!"
    print(has_special_chars(sample1))
    print(has_special_chars(sample2))
    print(has_special_chars(sample3))