def to_uppercase(s: str) -> str:
    return s.upper()
if __name__ == '__main__':
    test_string1 = "hello world"
    result1 = to_uppercase(test_string1)
    print(f"'{test_string1}' -> '{result1}'")
    test_string2 = "Python Programming"
    result2 = to_uppercase(test_string2)
    print(f"'{test_string2}' -> '{result2}'")
    test_string3 = "already UPPER"
    result3 = to_uppercase(test_string3)
    print(f"'{test_string3}' -> '{result3}'")